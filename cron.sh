killall PiMonitor
sleep 5
cd /home/pi/valet-tool
mv output.csv `date +%Y-%m-%d`-output.csv
sleep 5
/home/pi/valet-tool/PiMonitor | tee /home/pi/valet-tool/output.csv
