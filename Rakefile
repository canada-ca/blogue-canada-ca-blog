# Rakefile
task :copy_assets do
	sh "sh copy-assets.sh"
  end

  task :build => :copy_assets do
	sh "bundle exec jekyll build"
  end