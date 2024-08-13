#!/bin/bash

# Create necessary directories if they don't exist
mkdir -p en/css/
mkdir -p fr/css/
mkdir -p en/js/
mkdir -p fr/js/

# Copy CSS files
cp -r assets/css/*.css en/css/ || { echo "Failed to copy CSS files to en/css/"; exit 1; }
cp -r assets/css/*.css fr/css/ || { echo "Failed to copy CSS files to fr/css/"; exit 1; }

# Copy JS files
cp -r assets/js/*.js en/js/ || { echo "Failed to copy JS files to en/js/"; exit 1; }
cp -r assets/js/*.js fr/js/ || { echo "Failed to copy JS files to fr/js/"; exit 1; }

# Copy root files from assets to en/ and fr/
cp -r assets/* en/ || { echo "Failed to copy root files to en/"; exit 1; }
cp -r assets/* fr/ || { echo "Failed to copy root files to fr/"; exit 1; }