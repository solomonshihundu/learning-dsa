#########################################################################################################################################################
#							CLEARS ARCHIVE DIRECTORY EVERY 7 DAYS								#
#							UPDATED	: 30/06/2023										#	
#							VERSION : 4.0											#
#########################################################################################################################################################

#!/bin/bash

# directory paths to be cleaned
FILE_PATH_UG=/biload/FUGX/T24/archive

FILE_PATH_CI=/biload/FCIF/T24/archive

#directory path for logs
LOG_PATH=/export/home/oracle/tools/ClearDumps/logs/UG

#script directory
BASE_PATH=/export/home/oracle/tools/ClearDumps/scripts/UG

#Get todays date and name log file based on the date
LEO=$(perl -e 'use POSIX;print strftime "%Y%m%d",localtime time;')

#Define log file
LOG_FILE=${LOG_PATH}/archive-logs/Archive_MTN_ClearDMP_${LEO}.out 

############################################################################################################################

#Access UG archive folder
cd ${FILE_PATH_UG}

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
    LAST_FILE=$(ls -t $FILE_PATH_UG| head -1)

    #Start logging
    echo " UG Archive DMP File Clearing Started:" >> ${LOG_FILE}
	echo "********************************************************************************************" >> ${LOG_FILE}
	echo "Excluding ###### {$LAST_FILE} : \n" >> ${LOG_FILE}

    #File to be deleted
	echo "Dump Files to be deleted : " >> ${LOG_FILE}

    # loop through all files in the directory
    for file in "$FILE_PATH_UG"/*; do
    # exclude the most recently created file
    if [ "$file" != "$FILE_PATH_UG/$LAST_FILE" ]; then
        echo "$file" >> ${LOG_FILE}
        rm "$file"
    fi
    done

    echo "\n UG Archive Dump files successfully deleted." >> ${LOG_FILE}
	echo "*********************************************************************************************" >> ${LOG_FILE}

else
	echo "No changes made to Archive" >> ${LOG_FILE} 
	cd ${BASE_PATH}
fi

############################################################################################################################

#Access CI archive folder
cd ${FILE_PATH_CI}
  
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
    LAST_FILE=$(ls -t $FILE_PATH_CI| head -1)

    #Start logging
    echo " CI Archive DMP File Clearing Started:" >> ${LOG_FILE}
	echo "********************************************************************************************" >> ${LOG_FILE}
	echo "Excluding ###### {$LAST_FILE} : \n" >> ${LOG_FILE}

    #File to be deleted
	echo "Dump Files to be deleted : " >> ${LOG_FILE}

    # loop through all files in the directory
    for file in "$FILE_PATH_CI"/*; do
    # exclude the most recently created file
    if [ "$file" != "$FILE_PATH_CI/$LAST_FILE" ]; then
        echo "$file" >> ${LOG_FILE}
        rm "$file"
    fi
    done

    echo "\n CI Archive Dump files successfully deleted." >> ${LOG_FILE}
	echo "*********************************************************************************************" >> ${LOG_FILE}
	cd ${BASE_PATH}
    exit 0

else
	echo "No changes made to Archive" >> ${LOG_FILE} 
	cd ${BASE_PATH}
	exit 0
fi

#@auther : solomon.shihundu