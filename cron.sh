#!/bin/sh
tmux kill-session -t 'pimon'
cd /home/pi/valet-tool
python3 transformCSVtoTable.py
sh /home/pi/valet-tool/git.sh
tmux new-session -d -s 'pimon'
tmux send -t pimon.0 sh run.sh ENTER
