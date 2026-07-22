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

# Production build. Unchanged behavior except the old Netlify CONTEXT gate is
# gone and netlify.toml is excluded from the build (via _config.yml exclude).
task :build => :copy_assets do
  sh "bundle exec jekyll build"
end

namespace :staging do
  desc "Build the English staging preview into _staging/blog/"
  task :en => :copy_assets do
    build_staging("blog", "/blog/pr-preview/pr-#{require_pr_number}")
  end

  desc "Build the French staging preview into _staging/blogue/"
  task :fr => :copy_assets do
    build_staging("blogue", "/blogue/pr-preview/pr-#{require_pr_number}")
  end
end

# Full dual staging build used by the preview workflow.
desc "Build both EN and FR staging previews for PR_NUMBER=<n>"
task :staging => :copy_assets do
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
