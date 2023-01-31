FILE_PATH=/m8_mtn_todx
BASE_PATH=/export/home/oracle/tools/Xet/scripts/UG
COUNTRY=XUG

#Check if Conetxt is provided on execution
#If not use default context
if ! [ -z "$1" ]; 
then
   COUNTRY=$1
   echo "Using command line country $COUNTRY" 
else
   echo "Country defaulted to $COUNTRY" 
fi

#Access m8_mtn_todx folder
cd ${FILE_PATH}

#Get todays date and name log file based on the date
LEO=$(perl -e 'use POSIX;print strftime "%Y%m%d",localtime time;')
LOG_FILE=${BASE_PATH}/m8-mtn-logs/${COUNTRY}_ClearDMP_${LEO}.out

#Get File Count of files with XUG, Only proceed if count is greater then 1
COUNT=$(ls -dq *XUG* | wc -l)
echo $COUNT

#Check if file has 'XUG'
for FILE in *XUG*; 
	do 
	  echo $FILE; 
	done

cd ${BASE_PATH}







#Check if file has 'XUG' 
#if grep -q . "$XUG"; 
#then
#  Some Actions # SomeString was found
#fi
 
#Get File Count, Only proceed if count is greater then 1
#COUNT=$(find ./ -type f | wc -l)

#Cast to integer
#FILE_COUNT=$((COUNT))

#Log file count and time
#now=$(date +"%T")
#echo "File count is : {$FILE_COUNT}" >> ${LOG_FILE}

#cd ${BASE_PATH}





#if test $FILE_COUNT -gt 1
#then 
	#Get the last record in the folder 
	#Store in local variable
	#LAST_FILE=$(ls -Art1 | tail -1)

	#Start logging
        #echo "Archive DMP File Clearing Started:" >> ${LOG_FILE}
	#echo "********************************************************************************************" >> ${LOG_FILE}
	#echo "Excluding ###### {$LAST_FILE} : \n" >> ${LOG_FILE}

	#Add pathname expansion options
	#shopt -s extglob

	#File to be deleted
	#echo "Dump Files to be deleted :\n$(ls !($LAST_FILE))" >> ${LOG_FILE}

	#Remove all files in directory except
	#rm !($LAST_FILE)

	#echo "\nDump files successfully deleted." >> ${LOG_FILE}
	#echo "*********************************************************************************************" >> ${LOG_FILE}
	cd ${BASE_PATH}
	#exit 0
#else
	#echo "No changes made to Archive" >> ${LOG_FILE} 
	#exit 0
#fi