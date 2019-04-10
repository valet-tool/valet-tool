trap cleanup 2 # Trap cntrl C kill sig 2
WORKING_DIR=$(pwd)
TESTING_ACTIVE=false
function cleanup 
{
	if [ "$TESTING_ACTIVE" == true ]; then
		PiDUTSignal E
	fi
	cd $WORKING_DIR # Incase script sourced onto executing shell
	[ -e  $DOWNLOAD_LOCATION/test_file ] && rm $DOWNLOAD_LOCATION/test_file
	# http://mirrors.rit.edu/ubuntu-releases/18.10/ubuntu-18.10-desktop-amd64.iso
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
    DOWNLOAD_LINK="${i#*=}"
    shift # past argument=value
    ;;
    -w=*|--wait=*)
    DELAY_TESTS_IN_MIN="${i#*=}"
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

if [ "$DOWNLOAD_LINK" == "" ]; then
	echo "A URL was not provided for this test. Exiting..."
	exit 1
fi

if [ "$DELAY_TESTS_IN_MIN" == "" ]; then
    DELAY_TESTS_IN_MIN=60
    echo "You did not provide a delay to wait between tests. Defaulting to $(( "$DELAY_TESTS_IN_MIN" / 60 )) minute(s)..."
else 
    DELAY_TESTS_IN_MIN=$(( "$DELAY_TESTS_IN_MIN" * 60  ))
    echo "Delay interval set between tests is set to $(( "$DELAY_TESTS_IN_MIN" / 60 )) minute(s)..."
fi

cd $DOWNLOAD_LOCATION

while true; do
	 
	TESTING_ACTIVE=true
	PiDUTSignal B
	wget -O test_file $DOWNLOAD_LINK
	sync
	PiDUTSignal E
	TESTING_ACTIVE=false
	[ -e  $DOWNLOAD_LOCATION/test_file ] && rm $DOWNLOAD_LOCATION/test_file
	sync
	sleep $DELAY_TEST_IN_MIN
done

