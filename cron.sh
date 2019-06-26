#!/bin/sh
tmux kill-session -t 'pimon'
cd /home/pi/valet-tool
sh /home/pi/valet-tool/git.sh
tmux new-session -d -s 'pimon'
tmux send -t pimon.0 ./run.sh ENTER
