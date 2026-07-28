# Rakefile
#
# Build interface:
#   bundle exec rake build       -> production build into _site/
#   JEKYLL_ENV=staging PR_NUMBER=<n> bundle exec rake staging
#      -> copy_assets, then build the site TWICE with the staging config:
#         once with baseurl /blog/pr-preview/pr-<n>   into _staging/blog/
#         once with baseurl /blogue/pr-preview/pr-<n> into _staging/blogue/
#      Both builds use _config.yml + _config.staging.yml (staging last).
#      Fails loudly if PR_NUMBER is unset and asserts the staging config is
#      active (the staging Adobe analytics id must be present in the output).

STAGING_CONFIG = "_config.yml,_config.staging.yml"
STAGING_ANALYTICS_ID = "launch-913b1beddf7a-staging"

task :copy_assets do
  sh "sh copy-assets.sh"
end

# Custom-plugin guard (build security model). Jekyll's own `safe: true` was
# evaluated and rejected: this site's `jekyll-remote-theme` plugin supplies
# includes/layouts from a theme clone outside the source tree, and Jekyll's
# safe mode blocks exactly that kind of cross-boundary access, breaking every
# page (see docs/github-pages-setup.md "Build security model"). This task is
# the actual enforcement instead: it fails the build fast and loudly if a
# `_plugins/` directory exists at all, since no custom plugin is approved —
# the only approved plugin (jekyll-remote-theme) is a Gemfile/`plugins:`-
# declared gem, never a `_plugins/*.rb` file. Every build entry point below
# depends on this task.
task :guard_no_custom_plugins do
  if Dir.exist?("_plugins") && !Dir.empty?("_plugins")
    abort(<<~MSG)
      ERROR: a _plugins/ directory is present but not permitted.
      Custom Jekyll plugins are disabled in this repository. The only
      approved plugin is jekyll-remote-theme, declared via the Gemfile and
      _config.yml's `plugins:` key — never a _plugins/*.rb file. Remove
      _plugins/ before building.
    MSG
  end
end

# Production build. Plain `bundle exec rake build` is a pure production build.
# Transitional Netlify gate: when ENV['CONTEXT'] == 'deploy-preview' (set by
# Netlify on deploy previews), swap in the minimal _config.netlify-preview.yml
# so preview traffic uses the staging Adobe analytics id and stays out of
# production analytics. The minimal config carries ONLY the analytics override
# — it does NOT pull in _config.staging.yml (noindex, robots disallow, sitemap
# suppression, urlalt overrides), so deploy previews remain byte-equivalent to
# production except for the analytics id.
# Remove this gate after the Netlify decommission.
task :build => [:guard_no_custom_plugins, :copy_assets] do
  if ENV['CONTEXT'] == 'deploy-preview'
    sh "bundle exec jekyll build --config _config.yml,_config.netlify-preview.yml"
    normalize_preview_robots
  else
    sh "bundle exec jekyll build"
  end
end

# Transitional Netlify-preview normalization (remove after Netlify decommission).
# The minimal _config.netlify-preview.yml never sets `staging: true`, so deploy
# previews already avoid the staging disallow-all (`Disallow: /`) wired through
# the `site.staging` gate in en/robots.txt / fr/robots.txt. They do, however,
# inherit production's `Disallow: /images/` rule. Netlify deploy previews are
# temporary review surfaces that should be fully crawlable, so strip every
# `Disallow:` directive from the preview robots.txt after the build. Plain
# `rake build` is untouched and still ships the full production robots
# (`Disallow: /images/`), byte-equivalent to main.
def normalize_preview_robots
  Dir.glob("_site/**/robots.txt").each do |path|
    next unless File.file?(path)
    lines = File.readlines(path).reject { |line| line.strip.start_with?("Disallow:") }
    File.write(path, lines.join)
  end
end

namespace :staging do
  desc "Build the English staging preview into _staging/blog/"
  task :en => [:guard_no_custom_plugins, :copy_assets] do
    build_staging("blog", "/blog/pr-preview/pr-#{require_pr_number}")
  end

  desc "Build the French staging preview into _staging/blogue/"
  task :fr => [:guard_no_custom_plugins, :copy_assets] do
    build_staging("blogue", "/blogue/pr-preview/pr-#{require_pr_number}")
  end
end

# Full dual staging build used by the preview workflow.
desc "Build both EN and FR staging previews for PR_NUMBER=<n>"
task :staging => [:guard_no_custom_plugins, :copy_assets] do
  pr = require_pr_number
  build_staging("blog", "/blog/pr-preview/pr-#{pr}")
  build_staging("blogue", "/blogue/pr-preview/pr-#{pr}")
  assert_staging_active("_staging/blog")
  assert_staging_active("_staging/blogue")
  puts "Staging build complete for PR ##{pr}: _staging/blog and _staging/blogue"
end

def require_pr_number
  pr = ENV["PR_NUMBER"].to_s.strip
  if pr.empty?
    abort(<<~MSG)
      ERROR: PR_NUMBER is required for the staging build.
      Usage: JEKYLL_ENV=staging PR_NUMBER=<n> bundle exec rake staging
    MSG
  end
  pr
end

def build_staging(lang_root, baseurl)
  destination = File.join("_staging", lang_root)
  sh "JEKYLL_ENV=staging bundle exec jekyll build " \
     "--config #{STAGING_CONFIG} " \
     "--baseurl #{baseurl} " \
     "--destination #{destination}"
  rewrite_staging_assets(destination, baseurl)
end

# Staging-only post-processing pass (FR-224 image-404 fix). The Jekyll staging
# build prefixes template/theme asset references (those routed through Liquid
# filters like `relative_url` or baseurl-aware includes) with the preview
# baseurl, but CONTENT-authored references in posts -- raw
# `<img src="/images/foo.png">` in Markdown, plus `href` links to local files
# -- stay root-absolute and so resolve to the domain root under the preview
# subpath, 404'ing. This pass walks the built tree and prepends the baseurl to
# root-absolute `src`/`href`/`poster`/`srcset` values in *.html and `url(...)`
# values in *.css, leaving protocol-relative, full-URL, anchor, mailto:, tel:
# and data: values untouched. It is idempotent.
#
# This runs ONLY for staging; the production `build` task is unaffected and its
# `_site` output stays byte-identical. The config delta gate strips the baseurl
# prefix before comparing to production, so the extra prefixed references
# normalize back to the production form and the gate keeps passing.
def rewrite_staging_assets(dir, baseurl)
  script = File.join(".github", "scripts", "staging_asset_rewrite.py")
  sh "python3 #{script} --root #{dir} --baseurl #{baseurl}"
end

# Assert the staging configuration is actually active by verifying the staging
# Adobe analytics id is present in the built output (FR-21).
def assert_staging_active(dir)
  found = Dir.glob(File.join(dir, "**", "*.html")).any? do |path|
    File.read(path, mode: "rb").include?(STAGING_ANALYTICS_ID)
  end
  unless found
    abort "ERROR: staging analytics id '#{STAGING_ANALYTICS_ID}' not found " \
          "in #{dir}; the staging configuration was not active."
  end
  puts "OK: staging config verified in #{dir} (analytics id present)"
end
