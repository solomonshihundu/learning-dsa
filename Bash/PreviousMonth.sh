#!/bin/bash

# Get the current month
current_month=$(date +%m)

# Get the previous month (1-based)
previous_month=$((current_month - 1))

# If the previous month is 0, it means we're at January, so we set the previous month to December
if [ $previous_month -eq 0 ]; then
  previous_month=12
fi

# Find all files in the current directory with "XUG" in the name
for file in *XUG*; do
  # Get the file creation month (1-based)
  file_month=$(stat -c %y "$file" | cut -d '-' -f 2)

  # If the file was created in the previous month, delete it
  if [ $file_month -eq $previous_month ]; then
    echo "Deleting $file"
  fi
done
