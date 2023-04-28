#!/bin/bash

# set the dates
date1="20220315"
date2="20210903"

# convert the dates to seconds since epoch
epoch1=$(date -d "${date1:0:4}-${date1:4:2}-${date1:6:2}" "+%s")
epoch2=$(date -d "${date2:0:4}-${date2:4:2}-${date2:6:2}" "+%s")

# calculate the difference in seconds
diff=$((epoch1 - epoch2))

# convert the difference to days
days=$((diff / 86400))

echo "The difference between $date1 and $date2 is $days days."
