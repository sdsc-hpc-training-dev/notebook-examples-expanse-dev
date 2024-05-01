#!/bin/bash

# Get the current date and time
modified_date=$(date +"%Y-%m-%d %H:%M:%S")

# Replace the placeholder in the Markdown file with the current date and time
sed -i "s|{{last_modified_date}}|$modified_date|g" "$1"
