#!/bin/bash

tmux new -s backendserver -d
tmux send-keys "python3 main.py" C-m

cd /infra/frontend
tmux new -s frontendserver -d
tmux send-keys "npm start" C-m

while :
do
  sleep 1
done

exec "/bin/bash";
