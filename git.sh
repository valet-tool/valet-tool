cd /home/pi/valet-tool
git pull
sleep 2
git add /home/pi/valet-tool/rawfiles/*.csv
sleep 1
git commit -m "push data"
sleep 1
git push
