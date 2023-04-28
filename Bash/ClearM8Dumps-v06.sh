#       TEST CODE       #
###########################################################################################################################################

#!/bin/bash

#directory path to be cleaned
FILE_PATH=/export/home/oracle/tools/ClearDumps/test/dumps
#FILE_PATH=/m8_mtn_todx

#directory path for logs
LOG_PATH=/export/home/oracle/tools/ClearDumps/test/logs
#LOG_PATH=/export/home/oracle/tools/ClearDumps/logs/UG

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

#I4 Days Moving Baseline i.e (86400 seconds in a day X 14 days)
BASELINE=$(perl -e 'use POSIX;print strftime "%Y%m%d",localtime time-1209600;')

#Define log file
#LOG_FILE=${LOG_PATH}/m8-mtn-logs/${COUNTRY}_ClearDMP_${LEO}.out 
LOG_FILE=${LOG_PATH}/${COUNTRY}_ClearDMP_${LEO}_TEST.out 

#Access m8_mtn_todx directory
cd ${FILE_PATH}

#Start logging
echo "Archive DMP File Clearing Started:" >> ${LOG_FILE}
echo "********************************************************************************************" >> ${LOG_FILE}

echo "Clearing dump files Older than $BASELINE" >> ${LOG_FILE}

#File to be deleted
echo "Dump Files to be deleted : " >> ${LOG_FILE}

#Find all files in the current directory with "XUG" in the name
#and were created in the previous month
for file in *XUG*.dmp*; do
  #Get the file creation month (1-based)
 file_date=$(stat -c %y $file | cut -d ' ' -f1 | sed 's/-//g')

  #If the file was created in the previous month, delete it
 if [ $file_date -lt $BASELINE ]; then
    #File to be deleted
   echo "$file" >> ${LOG_FILE}
   rm "$file"
 fi
done

echo "\nDump files successfully deleted." >> ${LOG_FILE}
echo "*********************************************************************************************" >> ${LOG_FILE}

cd ${BASE_PATH}


#       ACTUAL CODE       #
###########################################################################################################################################



#!/bin/bash

#directory path to be cleaned
FILE_PATH=/m8_mtn_todx

#directory path for logs
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

#14 Days Moving Baseline i.e (86400 seconds in a day X 14 days)
BASELINE=$(perl -e 'use POSIX;print strftime "%Y%m%d",localtime time-1209600;')

#Define log file
LOG_FILE=${LOG_PATH}/m8-mtn-logs/${COUNTRY}_ClearDMP_${LEO}.out 

#Access m8_mtn_todx directory
cd ${FILE_PATH}

#Start logging
echo "Archive DMP File Clearing Started:" >> ${LOG_FILE}
echo "********************************************************************************************" >> ${LOG_FILE}

echo "Clearing dump files Older than $BASELINE" >> ${LOG_FILE}

#File to be deleted
echo "Dump Files to be deleted : " >> ${LOG_FILE}

#Find all files in the current directory with "XUG" in the file name
for file in *XUG*; 
do
	#Get the file creation date 
	file_date=$(stat -c %y $file | cut -d ' ' -f1 | sed 's/-//g')

  	#If the file was created a date later than the baseline date, delete it
 	if [ $file_date -lt $BASELINE ]; then
    		#File to be deleted
   		echo "$file" >> ${LOG_FILE}
   		rm "$file"
 	fi
done

echo "\nDump files successfully deleted." >> ${LOG_FILE}
echo "*********************************************************************************************" >> ${LOG_FILE}

cd ${BASE_PATH}

