killall PiMonitor
sleep(5)
cd /home/pi/valet-tool
mv output.csv `date +%Y-%m-%d`-output.csv
sleep(5)
/home/pi/PiPowerMeasure/PiMonitor | tee /home/pi/PiPowerMeasure/output.csv
