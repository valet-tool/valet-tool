trap cleanup 2 # Trap cntrl C kill sig 2
WORKING_DIR=$(pwd)
TESTING_ACTIVE=false
function cleanup 
{
	if [ "$TESTING_ACTIVE" == true ]; then
		PiDUTSignal E
	fi
	cd $WORKING_DIR # In case script sourced onto executing shell
	rm -rf $DOWNLOAD_LOCATION/*
	exit
}
#Collect provided options
for i in "$@"
do
case $i in
    -d=*|--download_dir=*)
    DOWNLOAD_LOCATION="${i#*=}"
    shift # past argument=value
    ;;
    -u=*|--test_url=*)
    DOWNLOAD_FILE="${i#*=}"
    shift # past argument=value
    ;;
    *)
    	echo "Incorrect option."
    	exit 1
    ;;
esac
done

if [ "$DOWNLOAD_LOCATION" == "" ]; then
	echo "A download location was not provided. Using $(pwd)"
	DOWNLOAD_LOCATION=$(pwd)
fi

if [ "$DOWNLOAD_FILE" == "" ]; then
	echo "A URL was not provided for this test. Exiting..."
	exit 1
fi


function doEverything(){
	compresedFileName="file.tar.gz"
    wget -q -O "$location/$compresedFileName" $1 >& /dev/null
	sync
	tar -xzf "$location/$compresedFileName" -C "$location/" 
	grep -r the "$location/" >& /dev/null
	extractedFileName=$(ls $location/ | awk '{print $1}' | grep -v $compresedFileName | grep -v file-zipped.tar.gz)
	tar czf "$location/file-zipped.tar.gz" "$location/$extractedFileName" 
}


export -f doEverything
export location=$DOWNLOAD_LOCATION

rm -rf $location/*

while true; do
	while read line; do	
		TESTING_ACTIVE=true
		PiDUTSignal B
		start=`date +%s`
		doEverything $line
		end=`date +%s`
		runtime=$((end-start))
		echo "$line,$runtime" >> `date +%Y-%m-%d-`recording.csv
		rm -rf $location/*
		sync
		PiDUTSignal E
		TESTING_ACTIVE=false
		sync
		sleep runtime
	done < "$DOWNLOAD_FILE"
done