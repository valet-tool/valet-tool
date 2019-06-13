killall PiMonitor
sleep 5
cd /home/pi/valet-tool
sleep 5
python3 transformCSVtoTable.py
sh /home/pi/valet-tool/git.sh
sleep 5
/home/pi/valet-tool/PiMonitor
