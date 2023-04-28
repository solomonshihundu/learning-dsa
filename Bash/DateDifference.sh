#!/bin/bash

# set the dates
date1="2022-03-15"
date2="2021-09-03"

# convert the dates to epoch time
epoch1=$(date -d "$date1" +%s)
epoch2=$(date -d "$date2" +%s)

# calculate the difference in seconds
diff=$(($epoch1 - $epoch2))

# convert the difference to days
days=$(($diff / 86400))

echo "The difference between $date1 and $date2 is $days days."
