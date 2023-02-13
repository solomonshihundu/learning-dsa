#!/bin/bash

# directory path to be cleaned
FILE_PATH=/export/home/oracle/tools/ClearDumps/test/dumps

#directory path for logs
#LOG_PATH=/export/home/oracle/tools/ClearDumps/logs/UG
LOG_PATH=/export/home/oracle/tools/ClearDumps/test

#script directory
BASE_PATH=/export/home/oracle/tools/ClearDumps/scripts/UG

#Default context if not provided
COUNTRY=UG

#Check if Conetxt is provided on execution
if ! [ -z "$1" ]; 
then
   COUNTRY=$1
   echo "Using command line country $COUNTRY" 
else
   echo "Country defaulted to $COUNTRY" 
fi

#Get todays date and name log file based on the date
LEO=$(perl -e 'use POSIX;print strftime "%Y%m%d",localtime time;')

#LOG_FILE=${LOG_PATH}/archive-logs/${COUNTRY}_ClearDMP_${LEO}.out 
LOG_FILE=${LOG_PATH}/logs/${COUNTRY}_ClearDMP_${LEO}_TEST2.out 


# Get the current date
current_date=$(date +%Y-%m-%d)

# Calculate the first day of the previous month
prev_month_start=$(date -d "$current_date -1 month" +%Y-%m-01)

# Calculate the last day of the previous month
prev_month_end=$(date -d "$prev_month_start +1 month -1 day" +%Y-%m-%d)

#Access M8- folder
cd ${FILE_PATH}


#Start logging
echo "Archive DMP File Clearing Started:" >> ${LOG_FILE}
echo "********************************************************************************************" >> ${LOG_FILE}

#File to be deleted
echo "Deletion in progress: " >> ${LOG_FILE}

# Use the calculated dates to delete files from the previous month
find $dir_path -type f -mtime +30 -print0 | xargs -0 rm -f

echo "\nDump files successfully deleted." >> ${LOG_FILE}
echo "*********************************************************************************************" >> ${LOG_FILE}

cd ${BASE_PATH}

