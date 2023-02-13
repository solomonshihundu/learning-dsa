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

#Access archive folder
cd ${FILE_PATH}

#Get todays date and name log file based on the date
LEO=$(perl -e 'use POSIX;print strftime "%Y%m%d",localtime time;')

#LOG_FILE=${LOG_PATH}/archive-logs/${COUNTRY}_ClearDMP_${LEO}.out 
LOG_FILE=${LOG_PATH}/logs/${COUNTRY}_ClearDMP_${LEO}_TEST.out    

#Get File Count, Only proceed if count is greater then 1
COUNT=$(find ./ -type f | wc -l)

#Cast to integer
FILE_COUNT=$((COUNT))

#Log file count and current time
now=$(date +"%T")
echo "File count is : {$FILE_COUNT} at $now" >> ${LOG_FILE}

if test $FILE_COUNT -gt 1
then 
    # get the most recently created file
    LAST_FILE=$(ls -t $FILE_PATH| head -1)

    #Start logging
    echo "Archive DMP File Clearing Started:" >> ${LOG_FILE}
	echo "********************************************************************************************" >> ${LOG_FILE}
	echo "Excluding ###### {$LAST_FILE} : \n" >> ${LOG_FILE}

    #File to be deleted
	echo "Dump Files to be deleted : " >> ${LOG_FILE}

    # loop through all files in the directory
    for file in "$FILE_PATH"/*; do
    # exclude the most recently created file
    if [ "$file" != "$FILE_PATH/$LAST_FILE" ]; then
        echo "$file" >> ${LOG_FILE}
        rm "$file"
    fi
    done

    echo "\nDump files successfully deleted." >> ${LOG_FILE}
	echo "*********************************************************************************************" >> ${LOG_FILE}
	cd ${BASE_PATH}
    #exit 0

else
	echo "No changes made to Archive" >> ${LOG_FILE} 
	cd ${BASE_PATH}
	#exit 0
fi