#!/bin/bash

# get today's Unix timestamp
now=$(date +%s)

# calculate the Unix timestamp for 14 days ago
baseline=$(date -d "@$((now - 1209600))" "+%Y%m%d")

echo "Today's date is $(date '+%Y%m%d')."
echo "The moving baseline 14 days ago is $baseline."


###########################################################################
baseline=$(perl -e 'use POSIX;print strftime "%Y%m%d",localtime time-1209600;')



stat -c %y XUG_20230111.dmp | cut -d ' ' -f1 | sed 's/-//g'
