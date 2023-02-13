#!/bin/bash

# directory path to be cleaned
#FILE_PATH=/export/home/oracle/tools/ClearDumps/test/dumps
FILE_PATH=/m8_mtn_todx

#directory path for logs
#LOG_PATH=/export/home/oracle/tools/ClearDumps/test
LOG_PATH=/export/home/oracle/tools/ClearDumps/logs/UG

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

#Define log file
LOG_FILE=${LOG_PATH}/m8-mtn-logs/${COUNTRY}_ClearDMP_${LEO}.out 

# Get the current month
current_month=$(date +%m)

# Get the previous month (1-based)
previous_month=$((current_month - 1))



# If the previous month is 0, it means we're at January, so we set the previous month to December
if [ $previous_month -eq 0 ]; then
  previous_month=12
fi

# Make sure previous_month is set to a numeric value
if [[ ! $previous_month =~ ^[0-9]+$ ]]; then
  previous_month=1
fi

#Access M8- folder
cd ${FILE_PATH}

#Start logging
echo "Archive DMP File Clearing Started:" >> ${LOG_FILE}
echo "********************************************************************************************" >> ${LOG_FILE}

#File to be deleted
echo "Dump Files to be deleted : " >> ${LOG_FILE}

# Find all files in the current directory with "XUG" in the name
# and were created in the previous month
for file in *XUG*; do
  # Get the file creation month (1-based)
  file_month=$(stat -c %y "$file" | cut -d '-' -f 2)

  # If the file was created in the previous month, delete it
  if [ $file_month -eq $previous_month ]; then
    #File to be deleted
    echo "$file" >> ${LOG_FILE}
    rm "$file"
  fi
done

echo "\nDump files successfully deleted." >> ${LOG_FILE}
echo "*********************************************************************************************" >> ${LOG_FILE}

cd ${BASE_PATH}
