# Rakefile
task :copy_assets do
  sh "sh copy-assets.sh"
end

task :build => :copy_assets do
  if ENV['CONTEXT'] == 'deploy-preview'
    sh "bundle exec jekyll build --config _config.yml,_config.staging.yml"
  else
    sh "bundle exec jekyll build"
  end
end