#!/bin/bash

# directory path to be cleaned
FILE_PATH=/export/home/oracle/tools/ClearDumps/test/dumps

#directory path for logs
#LOG_PATH=/export/home/oracle/tools/ClearDumps/logs/UG
LOG_PATH=/export/home/oracle/tools/ClearDumps/test

#Default context if not provided
COUNTRY=UG

#Get todays date and name log file based on the date
LEO=$(perl -e 'use POSIX;print strftime "%Y%m%d",localtime time;')

#LOG_FILE=${LOG_PATH}/archive-logs/${COUNTRY}_ClearDMP_${LEO}.out 
LOG_FILE=${LOG_PATH}/logs/${COUNTRY}_ClearDMP_${LEO}_TEST2.out 

# get the current month and year
current_month=$(date +%m)
current_year=$(date +%Y)

#Check if Conetxt is provided on execution
if ! [ -z "$1" ]; 
then
   COUNTRY=$1
   echo "Using command line country $COUNTRY" 
else
   echo "Country defaulted to $COUNTRY" 
fi

# calculate the previous month
if [ "$current_month" -eq 1 ]; then
  previous_month=12
  previous_year=$((current_year - 1))
else
  previous_month=$((current_month - 1))
  previous_year=$current_year
fi  

#Access M8- folder
cd ${FILE_PATH}

#File to be deleted
echo "Dump Files to be deleted : " >> ${LOG_FILE}

# loop through all files in the directory
for file in "$dir_path"/*; do
  # get the modified time of the file
  file_time=$(stat -c %y "$file" | cut -d' ' -f1)

  # extract the month and year from the modified time
  file_month=$(date -d "$file_time" +%m)
  file_year=$(date -d "$file_time" +%Y)

  # delete the file if it's from the previous month
  if [ "$file_month" -eq "$previous_month" ] && [ "$file_year" -eq "$previous_year" ]; then
    rm "$file"
  fi
done
