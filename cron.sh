killall PiMonitor
sleep(5)
mv output.log `date +%Y-%m-%d`-output.csv
sleep(5)
/home/pi/PiPowerMeasure/PiMonitor | tee /home/pi/PiPowerMeasure/output.csv