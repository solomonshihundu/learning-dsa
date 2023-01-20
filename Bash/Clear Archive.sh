FILE_PATH=/biload/FUGX/T24/archive
BASE_PATH=/export/home/oracle/tools/Xet/scripts/UG
COUNTRY=UG
CURRENT_DIR='.'

if ! [ -z "$1" ]; then
   COUNTRY=$1
   echo "Using command line country $COUNTRY"
else
   echo "Country defaulted to $COUNTRY"
fi

cd ${FILE_PATH}

#get_recent_file () {
#    FILE=$(ls -Art1 ${CURRENT_DIR} | tail -n 1)
#    if [ ! -f ${FILE} ]; then
#        CURRENT_DIR="${CURRENT_DIR}/${FILE}"
#        get_recent_file
#    fi
#    echo $FILE
#    exit
#}

get_recent_file () {
	FILE=$(ls -Art1 ${CURRENT_DIR} | tail -n 1)
	echo $FILE	
	exit
}

get_recent_file


ls -lhrt 

#echo "Enter log file name"

#User input log file name
#read NAME

#echo "Creating Log file"

#mklogs(){
#	mkdir "$NAME"
#	cd "$NAME"
#}

#mklogs

#echo "Currently in $NAME"

#cd ${FILE_PATH}
#LEO=$(perl -e 'use POSIX;print strftime "%Y%m%d",localtime time;')
#LOG_FILE=${BASE_PATH}/logs/${COUNTRY}_extr_${LEO}.out
#echo "Testing Log Output........." >>  ${LOG_FILE}
