#########################################################################################################################################################
#					CLEARS FILES OLDER THAN 14 DAYS IN M8_MTN_TODX DIRECTORY EVERY DAY						#
#							UPDATED	: 30/06/2023										#	
#							VERSION : 7.0											#
#########################################################################################################################################################

#!/bin/bash

#directory path to be cleaned
FILE_PATH=/m8_mtn_todx

#directory path for logs
LOG_PATH=/export/home/oracle/tools/ClearDumps/logs/UG

#script directory
BASE_PAH=/export/home/oracle/tools/ClearDumps/scripts/UG

#Get todays date and name log file based on the date
LEO=$(perl -e 'use POSIX;print strftime "%Y%m%d",localtime time;')

#14 Days Moving Baseline i.e (86400 seconds in a day X 5 days)
BASELINE=$(perl -e 'use POSIX;print strftime "%Y%m%d",localtime time-423000;')

#Define log file
LOG_FILE=${LOG_PATH}/m8-mtn-logs/M8_MTN_ClearDMP_${LEO}.out 

#Access m8_mtn_todx directory
cd ${FILE_PATH}

#Start logging
echo "M8 DMP File Clearing Started at : $(date +"%T")" >> ${LOG_FILE}
echo "********************************************************************************************" >> ${LOG_FILE}

echo "Clearing dump files Older than $BASELINE" >> ${LOG_FILE}

#File to be deleted
echo "Dump Files to be deleted : " >> ${LOG_FILE}

#Find all files in the current directory with "XUG" OR "XCI" in the file name
for file in *XUG* *XCI*; 
do
	#Get the file creation date 
	file_date=$(stat -c %y $file | cut -d ' ' -f1 | sed 's/-//g')

  	#If the file was created a date later than or equal to the baseline date, delete it
 	if [ $file_date -le $BASELINE ]; then
    		#File to be deleted
   		echo "$file" >> ${LOG_FILE}
   		rm "$file"
 	fi
done

echo "\nDump files successfully deleted." >> ${LOG_FILE}
echo "*********************************************************************************************" >> ${LOG_FILE}

cd ${BASE_PATH}

#@author : solomon.shihundu