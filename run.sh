!#/bin/sh
cd /home/pi/valet-tool
until PiMonitor; do
    echo "Server 'PiMonitor' crashed with exit code $?.  Respawning.." >&2
    sleep 1
done