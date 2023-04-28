#!/bin/bash

# set the reference date
baseline="20220101"

# convert the reference date to seconds since epoch
baseline_sec=$(date -d "${baseline:0:4}-${baseline:4:2}-${baseline:6:2}" "+%s")

# set the date to be compared
compare_date="20220315"

# convert the compare date to seconds since epoch
compare_date_sec=$(date -d "${compare_date:0:4}-${compare_date:4:2}-${compare_date:6:2}" "+%s")

# calculate the number of days between the baseline and compare date
days_since_baseline=$(( (compare_date_sec - baseline_sec) / 86400 ))

echo "The number of days since baseline $baseline to $compare_date is $days_since_baseline days."


#################################################################################################################


# get today's date in yyyymmdd format
today=$(date "+%Y%m%d")

# calculate the baseline date 14 days ago
baseline=$(date -d "$today - 14 days" "+%Y%m%d")

echo "Today's date is $today."
echo "The moving baseline 14 days ago is $baseline."