#!/bin/bash
sudo apt-get update
sudo apt-get install -y docker.io
sudo chmod 777 /var/run/docker.sock
docker pull ${var.docker_image}
docker run -d --rm --name web-test -p 80:8000 ${var.docker_image}
