#import paramiko
#ssh = paramiko.SSHClient()
#ssh.connect('20.161.7.53', username='azureuser', password='@Password@123')
#ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls')

import paramiko
docker_image = 'crccheck/hello-world'

command = "sudo apt-get update && sudo apt-get install -y docker.io && sudo chmod 777 /var/run/docker.sock && docker pull " + docker_image + " && docker run -d --rm --name web-test -p 80:8000 " + docker_image

# Update the next three lines with your
# server's information

host = "20.161.7.53"
username = "azureuser"
password = "@Password@123"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
_stdin, _stdout,_stderr = client.exec_command(command)
print(_stdout.read().decode())
client.close()
