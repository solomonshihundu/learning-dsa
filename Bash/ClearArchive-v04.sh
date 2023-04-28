#########################################################################################################################################################
#							CLEARS ARCHIVE DIRECTORY EVERY 7 DAYS								#
#							UPDATED	: 04/04/2023										#	
#							VERSION : 3.0											#
#########################################################################################################################################################

#!/bin/bash

# directories to be cleaned
UG_FILE_PATH=/biload/FUGX/T24/archive #UG
CI_FILE_PATH=/biload/FCIF/T24/archive #CI

#directory path for logs
LOG_PATH=/export/home/oracle/tools/ClearDumps/logs

#script directory
BASE_PATH=/export/home/oracle/tools/ClearDumps/scripts/UG

#Get todays date and name log file based on the date
LEO=$(perl -e 'use POSIX;print strftime "%Y%m%d",localtime time;')

#Define log file
LOG_FILE=${LOG_PATH}/archive-logs/${COUNTRY}_ClearDMP_${LEO}.out 

########################################################################################################
#Access UG archive folder
cd ${UG_FILE_PATH}

echo "Clearing UG Archive folder :" >> ${LOG_FILE}
  
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
    LAST_FILE=$(ls -t $UG_FILE_PATH| head -1)

    #Start logging
    echo "Archive DMP File Clearing Started:" >> ${LOG_FILE}
	echo "********************************************************************************************" >> ${LOG_FILE}
	echo "Excluding ###### {$LAST_FILE} : \n" >> ${LOG_FILE}

    #File to be deleted
	echo "Dump Files to be deleted : " >> ${LOG_FILE}

    # loop through all files in the directory
    for file in "$UG_FILE_PATH"/*; do
    # exclude the most recently created file
    if [ "$file" != "$UG_FILE_PATH/$LAST_FILE" ]; then
        echo "$file" >> ${LOG_FILE}
        rm "$file"
    fi
    done

    echo "\nDump files successfully deleted." >> ${LOG_FILE}
	echo "*********************************************************************************************" >> ${LOG_FILE}

else
	echo "No changes made to UG Archive" >> ${LOG_FILE} 
	cd ${BASE_PATH}
fi

########################################################################################################
#Access CI archive folder
cd ${UG_FILE_PATH}

echo "Clearing CI Archive folder :" >> ${LOG_FILE}
  
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
    LAST_FILE=$(ls -t $CI_FILE_PATH| head -1)

    #Start logging
    echo "Archive DMP File Clearing Started:" >> ${LOG_FILE}
	echo "********************************************************************************************" >> ${LOG_FILE}
	echo "Excluding ###### {$LAST_FILE} : \n" >> ${LOG_FILE}

    #File to be deleted
	echo "Dump Files to be deleted : " >> ${LOG_FILE}

    # loop through all files in the directory
    for file in "$CI_FILE_PATH"/*; do
    # exclude the most recently created file
    if [ "$file" != "$CI_FILE_PATH/$LAST_FILE" ]; then
        echo "$file" >> ${LOG_FILE}
        rm "$file"
    fi
    done

    echo "\nDump files successfully deleted." >> ${LOG_FILE}
	echo "*********************************************************************************************" >> ${LOG_FILE}
	cd ${BASE_PATH}
    #exit 0

else
	echo "No changes made to CI Archive" >> ${LOG_FILE} 
	cd ${BASE_PATH}
	#exit 0
fi

#@auther : solomon.shihundu