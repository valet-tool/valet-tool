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
	randomizer=${RANDOM}
	mkdir "$location${randomizer}"
	start=`date +%s`
    wget -q -O "${randomizer}.tar.gz" $0 >& /dev/null
	sync
	tar -xzf "${randomizer}.tar.gz" -C "$location${randomizer}"
	grep -r the "$location${randomizer}" >& /dev/null
	tar -czf "${randomizer}-zipped.tar.gz" "$location${randomizer}/"
	end=`date +%s`
	runtime=$((end-start))
	echo "$0,$runtime" >> recording.csv
	[ -e  "$location${randomizer}" ] && rm -rf "$location${randomizer}"
	[ -e  "${randomizer}.tar.gz" ] && rm "${randomizer}.tar.gz"
	[ -e  "${randomizer}-zipped.tar.gz" ] && rm "${randomizer}-zipped.tar.gz"
}

TESTING_ACTIVE=true
PiDUTSignal B

export -f doEverything
export location=$DOWNLOAD_LOCATION

IFS=$'\n' read -d '' -r -a lines < $DOWNLOAD_FILE
printf '%s\0' "${lines[@]}" | xargs -n 1 -P 8 -0 bash -c 'doEverything "$@"'
    
sync
PiDUTSignal E

TESTING_ACTIVE=false
sync
