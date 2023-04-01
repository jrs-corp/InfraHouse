#!/bin/bash

export AWS_ACCESS_KEY_ID=$(AWS_ACCESS_KEY_ID)
export AWS_SECRET_ACCESS_KEY=$(AWS_SECRET_ACCESS_KEY)

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
