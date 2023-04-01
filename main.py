from flask import Flask
from flask import request
from flask_cors import CORS
import subprocess
import paramiko
import time


app = Flask(__name__)
CORS(app)

@app.route("/")
def start():
    temp_data = {"status":200, "response":"Main Page"} 
    return temp_data

@app.route("/toutes", methods=['POST'])
def toutes():
    platform=request.get_json()['platform']
    codelocation=request.get_json()['codelocation']
    print(platform, codelocation)
    temp_data = {"result": "It will be deployed in the given settings"}
    print('TEMP_DATA')
    print(temp_data)
    return temp_data


@app.route("/configuration", methods=['POST'])
def configuration():
    # print(request.get_json())
    platform = request.get_json()['platform']
    codelocation = request.get_json()['codelocation']
    imagelocation = request.get_json()['imagelocation']
    print(platform, codelocation)
    subprocess.run(["pwd"])
    # subprocess.Popen("ls", cwd="/")
    # subprocess.run(["terraform init"], shell=True)
    subprocess.call('cd ' + platform + ' && terraform init -upgrade', shell=True)
    subprocess.call('cd ' + platform + ' && terraform plan', shell=True)
    
    subprocess.call('cd ' + platform + ' && terraform apply -var "docker_image=' + imagelocation + '" -auto-approve', shell=True)
    # result = subprocess.check_output('cd ' + platform + ' && terraform apply -auto-approve', shell=True)
    subprocess.call('cd ' + platform + ' && terraform output', shell=True)
    # print(result)
    print('CHECK THE OUTPUT NOW----------------------')
        #subprocess.call('export MY_OUTPUT_VARIABLE=$(terraform output instance_public_ip)', shell=True)
    #subprocess.call('echo $MY_OUTPUT_VARIABLE', shell=True)
    # print(result)

    if (platform=="azure"):
        print('Azure code here')
        time.sleep(60)
        subprocess.call('cd ' + platform + ' && terraform output public_ip_address > terraform_output', shell=True)


        docker_image = imagelocation
        command = "sudo apt-get update && sudo apt-get install -y docker.io && sudo chmod 777 /var/run/docker.sock && docker pull " + docker_image + " && docker run -d --rm --name web-test -p 80:8000 " + docker_image


        # Update the next three lines with your
        # server's information
        f = open("azure/terraform_output", "r")
        tempData = f.read()
        print('tempData')
        print(tempData[1:-2])
        print('ENDDDDDDDDDDDDDDDDDDDDDDd')

        host = tempData[1:-2]
        username = "azureuser"
        password = "@Password@123"
        import paramiko
        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        _stdin, _stdout,_stderr = client.exec_command(command)
        print(_stdout.read().decode())
        client.close()

        # Define the SSH command to run
        #ssh_command = "sshpass -p '@Password@123' ssh azureuser@20.161.7.53"

        # Define the Docker installation command to run on the remote server
        #docker_install_command = 'sudo apt-get update && sudo apt-get install -y docker.io'

        # Combine the commands with a pipe
        #combined_command = ssh_command + ' "' + docker_install_command + '"'

        # Run the combined command with subprocess
        #process = subprocess.Popen(combined_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait for the command to complete and capture the output
        #stdout, stderr = process.communicate()
        
        # Print the output
        #print(stdout.decode())
        #print(stderr.decode())
        f = open("azure/terraform_output", "r")
        tempData = f.read()
        print('tempData')
        print(tempData[1:-2])
        print('ENDDDDDDDDDDDDDDDDDDDDDDd')
        temp_data = {
                "result": tempData[1:-2],
                "pem": "@Password@123"
                }

#        temp_data = {
#                "result": "20.161.7.53",
#                "password": "@Password@123"
#                }
        return temp_data
    elif (platform == "gcp"):

        print('GCP code here')
        time.sleep(60)
        subprocess.call('cd ' + platform + ' && terraform output public_ip > terraform_output', shell=True)

        f = open("gcp/terraform_output", "r")
        tempData = f.read()
        print('tempData')
        print(tempData[1:-2])

        import paramiko
        docker_image = imagelocation#'crccheck/hello-world'
        command = "sudo apt-get update && sudo apt-get install -y docker.io && sudo chmod 777 /var/run/docker.sock && docker pull " + docker_image + " && docker run -d --rm --name web-test -p 80:8000 " + docker_image
        # Set the key filename
        key_filename = 'aws/terraform_ec2_key'

        # Create an SSH client object
        ssh = paramiko.SSHClient()

        # Automatically add the host key (not recommended for production use)
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Load the private key
        key = paramiko.RSAKey.from_private_key_file(key_filename)

        # Connect to the remote instance using SSH key authentication
        ssh.connect(hostname=tempData[1:-2], username='ubuntu', pkey=key)

        # Now you can run commands on the remote instance via the SSH connection, for example:
        stdin, stdout, stderr = ssh.exec_command(command)
        print(stdout.read())

        # Close the SSH connection when finished
        ssh.close()
        f = open("gcp/terraform_output", "r")
        tempData = f.read()
        print('tempData')
        print(tempData[1:-2])
        print('ENDDDDDDDDDDDDDDDDDDDDDDd')
        temp_data = {
                "result": tempData[1:-2],
                "pem": """
                -----BEGIN OPENSSH PRIVATE KEY-----
                b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAACFwAAAAdzc2gtcn
                NhAAAAAwEAAQAAAgEAyV/w/2wm+0OJ9ZHMpojex68pfnNwVDc8LxOZQbuOwMDT3N53F0ei
                Wmv/ZtCfOuq6HZguqhKOOeKeCWSedCR1ikh0KCmw2MV0puoW+VjSaZombnc6DORqXz7Yqg
                lyIZy77VFm5IUXcEvwdmEog1x2BAEQKgQgduDkYBWxln5U/NfVuAMVZt7h2oV+rwbO68h5
                HnY9InaEbVft2SnQmTqTawPac3nTmjZy71PdJSNgJLH9t01KVRIXLmOvaCDda1tTiILroO
                ZUdIunJJFWSdJXzLR5Z37CiG216GzK+ecMVK2QaW526j3k4TG38ECnqJ2VVIXzST66810S
                67DhJxUeXmnrJ40OFFSh+1/IKGYNqa1fV04tjOCw4DMLBsybHZU4fn9YVJK9AyHnTHxzgW
                3Lx3HJ0/hXsxnDN/LqFP4zNn2CNRXXnjRLRulQx5zm6ZQftLLFUgRIkZHysk146VV7Vf3F
                XYBUi78uygRnOia2toeTZDzg+j17+WaxotnT/oYa6EY+GnEm1YsO26mGhIhZB8s5FXMtZV
                X10ByV67VhTX6oClo4p6EW9/x6KmgNfMZY8icdA0Bbo93HPu6vZpB7mnGuurHm5nZyrhZD
                rkGB7wbwWAOFvN8t95GlTJCOUPyjLaIDYbfvmZggepBZ14DVMHf8jZYqD7ajhaKT0OPq6N
                MAAAdI3kAXZt5AF2YAAAAHc3NoLXJzYQAAAgEAyV/w/2wm+0OJ9ZHMpojex68pfnNwVDc8
                LxOZQbuOwMDT3N53F0eiWmv/ZtCfOuq6HZguqhKOOeKeCWSedCR1ikh0KCmw2MV0puoW+V
                jSaZombnc6DORqXz7YqglyIZy77VFm5IUXcEvwdmEog1x2BAEQKgQgduDkYBWxln5U/NfV
                uAMVZt7h2oV+rwbO68h5HnY9InaEbVft2SnQmTqTawPac3nTmjZy71PdJSNgJLH9t01KVR
                IXLmOvaCDda1tTiILroOZUdIunJJFWSdJXzLR5Z37CiG216GzK+ecMVK2QaW526j3k4TG3
                8ECnqJ2VVIXzST66810S67DhJxUeXmnrJ40OFFSh+1/IKGYNqa1fV04tjOCw4DMLBsybHZ
                U4fn9YVJK9AyHnTHxzgW3Lx3HJ0/hXsxnDN/LqFP4zNn2CNRXXnjRLRulQx5zm6ZQftLLF
                UgRIkZHysk146VV7Vf3FXYBUi78uygRnOia2toeTZDzg+j17+WaxotnT/oYa6EY+GnEm1Y
                sO26mGhIhZB8s5FXMtZVX10ByV67VhTX6oClo4p6EW9/x6KmgNfMZY8icdA0Bbo93HPu6v
                ZpB7mnGuurHm5nZyrhZDrkGB7wbwWAOFvN8t95GlTJCOUPyjLaIDYbfvmZggepBZ14DVMH
                f8jZYqD7ajhaKT0OPq6NMAAAADAQABAAACAApKWdFjoHZUlDc1VSTpd6DypYcttP7It82c
                DcfbIsdc0zbFM4bABV7jh/CkFo73Mb2TakcMnbH9j5/hQWuj9VG0tCLdRok9ReHFspjZXh
                9BXldkxlWkUn89germgquPC9drwntJBdKaPtZ9zokv72Py/fV3soUApwr18NZE7GjjSquV
                lMFmAFqfWcLt8SMBYpcY6bTaI5hG1wOy7FL4OFJOpxohjpuhzqvGOFXOgfo+Ej4MuBCy1P
                Zs56jFjSsQRquCLTJSstwlysvGlYc+NXhjfJS6WIyKNrKC5LhygyHMoMWSfIcp1IlhdgnT
                8/1c2CWylqUWjI0lI3Nh3Y+Wt696MwJHq0x8i3/J6Xj16Un6uL/GPtVPAq94kkebLhxrkT
                cwAdslxRlQXnAelYzTr1r586MNswximPP13hyugZiF9tcEOLag9nw3dRyuemU5c2N5r5U/
                ouUpQ+57mB/heTLVBWgFZY3mpNW3+uYOY+u1UypHSVtUDL4dPgH3An5PskWGuDw85vCoz7
                gd6PSBr5wy6YnT5ZKDBa7z6ahlcdo0eMbrTuno6CmrfnKhjvBanhsDwDPMVNtJrvly/qR+
                ZhEMF1T0efEYxM/BdIWV1WlLkh3/gfBwvOdJ7ykslGGnntf1yVff8CZ40tlwjW2VOLMbJx
                lNo/TTrdMJb6MFh8pBAAABAEKyusYaJuCblcbdQ0+C82Cu6Vbf/kpOGr+FUrk1oRrO/hrE
                aMrAfDJF+5jNeXVaLriUqnAJ7Z1lJg6O+gzRVktP1FnZCIl8u0XF9naxcMOJg0Z6MNxrXe
                5C71Txb6a4Rs7AlwUbAQ/3VdmhqmtjnOVr1RDf7Duo7F1mJ1Q2ydxgdUKx9fgLkyNnHUKc
                gqG1Q0CXRPqgg1KCpsCVU4ba+f3mdC1h06l1huFwGlHph4sxvPwcBRhaAO4IVuVpwS3vrs
                y0/cw+j/fXjo3BS+8nbqy1WtCUpRfB+jzb8ogTBfRzUKO9ghoRTHSAro3Ths17hjzwJCUq
                i14dPrL75BF8MM4AAAEBANcr109kjl3cg5jTXK6u1X6iii6c0ZiiwmO84OlgDYiKSp4AZL
                8Qj24R3+MbbL7o30nFIvMnBe/wfAo1LdIqR3iyw7XtHEn7TJfplWhah3VJo8Q4ognPAjb0
                WkIPYoq1HvnZJHCskQbtEA4ltmOZWp8rUKPnyBLo53Y3xwx40j43SNDnvKUgcna2OfhlG3
                kMyOvd6w1Up2XaCuy7EDoySm4g1WJe+1jMFKwjJPBrZr4iyxXAl5JzYp5zSoqtn1p5Ldc4
                fBOZ7/9scnEnvGkWQDbhsv3r9L/nDQrAKGXcGoyjF0t27LzYhkNTSJpS6dJQxJMGd+yScd
                NOZmqdm/SGUfMAAAEBAO+V7CDMwCW1AfNZLBQmgBjR3Glv5WmJYOe1e3dRaffqnA1LKM3E
                1IRiCa7ZYxfm6Fy3LiDHB2P3/pQ77oocusRX0InnFD9h2elXl3Gx8DxLozvToSHUsVv67G
                A3ChJRFZgL8Uxh79ma57AJQGVS3CgXYq3en8BRA0OOyZuid7abciExwSjPdaxvL+ZneYWe
                gS7f4vgMFDGuANdxWHQ1YiHOHTBGvLsZ2Gi3LJrAl7We0/zbupoPHalBN2546XQJWKPpXF
                5T4ANz9jdlP472G2+12nuNtUQYXJbCqIFp9U9ScivyryF2Iu1aSNzPzei+Vqe3cd6y3tBm
                4L8iRzER5aEAAAATZXhhbXBsZUBleGFtcGxlLmNvbQ==
                -----END OPENSSH PRIVATE KEY-----
                """
                }
        return temp_data
    elif (platform == "oracle"):
        print('Oracle code here')
        time.sleep(60)
        subprocess.call('cd ' + platform + ' && terraform output public_ip > terraform_output', shell=True)

        f = open("oracle/terraform_output", "r")
        tempData = f.read()
        print('tempData')
        print(tempData[1:-2])

        import paramiko
        docker_image = imagelocation#'crccheck/hello-world'
        command = "sudo apt-get update && sudo apt-get install -y docker.io && sudo chmod 777 /var/run/docker.sock && docker pull " + docker_image + " && docker run -d --rm --name web-test -p 80:8000 " + docker_image
        # Set the key filename
        key_filename = 'aws/terraform_ec2_key'

        # Create an SSH client object
        ssh = paramiko.SSHClient()

        # Automatically add the host key (not recommended for production use)
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Load the private key
        key = paramiko.RSAKey.from_private_key_file(key_filename)

        # Connect to the remote instance using SSH key authentication
        ssh.connect(hostname=tempData[1:-2], username='ubuntu', pkey=key)

        # Now you can run commands on the remote instance via the SSH connection, for example:
        stdin, stdout, stderr = ssh.exec_command(command)
        print(stdout.read())

        # Close the SSH connection when finished
        ssh.close()
        f = open("oracle/terraform_output", "r")
        tempData = f.read()
        print('tempData')
        print(tempData[1:-2])
        print('ENDDDDDDDDDDDDDDDDDDDDDDd')
        temp_data = {
                "result": tempData[1:-2],
                "pem": """
                -----BEGIN OPENSSH PRIVATE KEY-----
                b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAACFwAAAAdzc2gtcn
                NhAAAAAwEAAQAAAgEAyV/w/2wm+0OJ9ZHMpojex68pfnNwVDc8LxOZQbuOwMDT3N53F0ei
                Wmv/ZtCfOuq6HZguqhKOOeKeCWSedCR1ikh0KCmw2MV0puoW+VjSaZombnc6DORqXz7Yqg
                lyIZy77VFm5IUXcEvwdmEog1x2BAEQKgQgduDkYBWxln5U/NfVuAMVZt7h2oV+rwbO68h5
                HnY9InaEbVft2SnQmTqTawPac3nTmjZy71PdJSNgJLH9t01KVRIXLmOvaCDda1tTiILroO
                ZUdIunJJFWSdJXzLR5Z37CiG216GzK+ecMVK2QaW526j3k4TG38ECnqJ2VVIXzST66810S
                67DhJxUeXmnrJ40OFFSh+1/IKGYNqa1fV04tjOCw4DMLBsybHZU4fn9YVJK9AyHnTHxzgW
                3Lx3HJ0/hXsxnDN/LqFP4zNn2CNRXXnjRLRulQx5zm6ZQftLLFUgRIkZHysk146VV7Vf3F
                XYBUi78uygRnOia2toeTZDzg+j17+WaxotnT/oYa6EY+GnEm1YsO26mGhIhZB8s5FXMtZV
                X10ByV67VhTX6oClo4p6EW9/x6KmgNfMZY8icdA0Bbo93HPu6vZpB7mnGuurHm5nZyrhZD
                rkGB7wbwWAOFvN8t95GlTJCOUPyjLaIDYbfvmZggepBZ14DVMHf8jZYqD7ajhaKT0OPq6N
                MAAAdI3kAXZt5AF2YAAAAHc3NoLXJzYQAAAgEAyV/w/2wm+0OJ9ZHMpojex68pfnNwVDc8
                LxOZQbuOwMDT3N53F0eiWmv/ZtCfOuq6HZguqhKOOeKeCWSedCR1ikh0KCmw2MV0puoW+V
                jSaZombnc6DORqXz7YqglyIZy77VFm5IUXcEvwdmEog1x2BAEQKgQgduDkYBWxln5U/NfV
                uAMVZt7h2oV+rwbO68h5HnY9InaEbVft2SnQmTqTawPac3nTmjZy71PdJSNgJLH9t01KVR
                IXLmOvaCDda1tTiILroOZUdIunJJFWSdJXzLR5Z37CiG216GzK+ecMVK2QaW526j3k4TG3
                8ECnqJ2VVIXzST66810S67DhJxUeXmnrJ40OFFSh+1/IKGYNqa1fV04tjOCw4DMLBsybHZ
                U4fn9YVJK9AyHnTHxzgW3Lx3HJ0/hXsxnDN/LqFP4zNn2CNRXXnjRLRulQx5zm6ZQftLLF
                UgRIkZHysk146VV7Vf3FXYBUi78uygRnOia2toeTZDzg+j17+WaxotnT/oYa6EY+GnEm1Y
                sO26mGhIhZB8s5FXMtZVX10ByV67VhTX6oClo4p6EW9/x6KmgNfMZY8icdA0Bbo93HPu6v
                ZpB7mnGuurHm5nZyrhZDrkGB7wbwWAOFvN8t95GlTJCOUPyjLaIDYbfvmZggepBZ14DVMH
                f8jZYqD7ajhaKT0OPq6NMAAAADAQABAAACAApKWdFjoHZUlDc1VSTpd6DypYcttP7It82c
                DcfbIsdc0zbFM4bABV7jh/CkFo73Mb2TakcMnbH9j5/hQWuj9VG0tCLdRok9ReHFspjZXh
                9BXldkxlWkUn89germgquPC9drwntJBdKaPtZ9zokv72Py/fV3soUApwr18NZE7GjjSquV
                lMFmAFqfWcLt8SMBYpcY6bTaI5hG1wOy7FL4OFJOpxohjpuhzqvGOFXOgfo+Ej4MuBCy1P
                Zs56jFjSsQRquCLTJSstwlysvGlYc+NXhjfJS6WIyKNrKC5LhygyHMoMWSfIcp1IlhdgnT
                8/1c2CWylqUWjI0lI3Nh3Y+Wt696MwJHq0x8i3/J6Xj16Un6uL/GPtVPAq94kkebLhxrkT
                cwAdslxRlQXnAelYzTr1r586MNswximPP13hyugZiF9tcEOLag9nw3dRyuemU5c2N5r5U/
                ouUpQ+57mB/heTLVBWgFZY3mpNW3+uYOY+u1UypHSVtUDL4dPgH3An5PskWGuDw85vCoz7
                gd6PSBr5wy6YnT5ZKDBa7z6ahlcdo0eMbrTuno6CmrfnKhjvBanhsDwDPMVNtJrvly/qR+
                ZhEMF1T0efEYxM/BdIWV1WlLkh3/gfBwvOdJ7ykslGGnntf1yVff8CZ40tlwjW2VOLMbJx
                lNo/TTrdMJb6MFh8pBAAABAEKyusYaJuCblcbdQ0+C82Cu6Vbf/kpOGr+FUrk1oRrO/hrE
                aMrAfDJF+5jNeXVaLriUqnAJ7Z1lJg6O+gzRVktP1FnZCIl8u0XF9naxcMOJg0Z6MNxrXe
                5C71Txb6a4Rs7AlwUbAQ/3VdmhqmtjnOVr1RDf7Duo7F1mJ1Q2ydxgdUKx9fgLkyNnHUKc
                gqG1Q0CXRPqgg1KCpsCVU4ba+f3mdC1h06l1huFwGlHph4sxvPwcBRhaAO4IVuVpwS3vrs
                y0/cw+j/fXjo3BS+8nbqy1WtCUpRfB+jzb8ogTBfRzUKO9ghoRTHSAro3Ths17hjzwJCUq
                i14dPrL75BF8MM4AAAEBANcr109kjl3cg5jTXK6u1X6iii6c0ZiiwmO84OlgDYiKSp4AZL
                8Qj24R3+MbbL7o30nFIvMnBe/wfAo1LdIqR3iyw7XtHEn7TJfplWhah3VJo8Q4ognPAjb0
                WkIPYoq1HvnZJHCskQbtEA4ltmOZWp8rUKPnyBLo53Y3xwx40j43SNDnvKUgcna2OfhlG3
                kMyOvd6w1Up2XaCuy7EDoySm4g1WJe+1jMFKwjJPBrZr4iyxXAl5JzYp5zSoqtn1p5Ldc4
                fBOZ7/9scnEnvGkWQDbhsv3r9L/nDQrAKGXcGoyjF0t27LzYhkNTSJpS6dJQxJMGd+yScd
                NOZmqdm/SGUfMAAAEBAO+V7CDMwCW1AfNZLBQmgBjR3Glv5WmJYOe1e3dRaffqnA1LKM3E
                1IRiCa7ZYxfm6Fy3LiDHB2P3/pQ77oocusRX0InnFD9h2elXl3Gx8DxLozvToSHUsVv67G
                A3ChJRFZgL8Uxh79ma57AJQGVS3CgXYq3en8BRA0OOyZuid7abciExwSjPdaxvL+ZneYWe
                gS7f4vgMFDGuANdxWHQ1YiHOHTBGvLsZ2Gi3LJrAl7We0/zbupoPHalBN2546XQJWKPpXF
                5T4ANz9jdlP472G2+12nuNtUQYXJbCqIFp9U9ScivyryF2Iu1aSNzPzei+Vqe3cd6y3tBm
                4L8iRzER5aEAAAATZXhhbXBsZUBleGFtcGxlLmNvbQ==
                -----END OPENSSH PRIVATE KEY-----
                """
                }
        return temp_data

    elif (platform == "aws"):
        subprocess.call('cd ' + platform + ' && terraform output instance_public_ip > terraform_output', shell=True)
        time.sleep(60)

        f = open("aws/terraform_output", "r")
        tempData = f.read()
        print('tempData')
        print(tempData[1:-2])

        import paramiko
        docker_image = imagelocation#'crccheck/hello-world'
        command = "sudo apt-get update && sudo apt-get install -y docker.io && sudo chmod 777 /var/run/docker.sock && docker pull " + docker_image + " && docker run -d --rm --name web-test -p 80:8000 " + docker_image
        # Set the key filename
        key_filename = 'aws/terraform_ec2_key'

        # Create an SSH client object
        ssh = paramiko.SSHClient()

        # Automatically add the host key (not recommended for production use)
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Load the private key
        key = paramiko.RSAKey.from_private_key_file(key_filename)

        # Connect to the remote instance using SSH key authentication
        ssh.connect(hostname=tempData[1:-2], username='ubuntu', pkey=key)

        # Now you can run commands on the remote instance via the SSH connection, for example:
        stdin, stdout, stderr = ssh.exec_command(command)
        print(stdout.read())

        # Close the SSH connection when finished
        ssh.close()

        f = open("aws/terraform_output", "r")
        tempData = f.read()
        print('tempData')
        print(tempData[1:-2])
        print('ENDDDDDDDDDDDDDDDDDDDDDDd')
        temp_data = {
                "result": tempData[1:-2],
                "pem": """
                -----BEGIN OPENSSH PRIVATE KEY-----
                b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAACFwAAAAdzc2gtcn
                NhAAAAAwEAAQAAAgEAyV/w/2wm+0OJ9ZHMpojex68pfnNwVDc8LxOZQbuOwMDT3N53F0ei
                Wmv/ZtCfOuq6HZguqhKOOeKeCWSedCR1ikh0KCmw2MV0puoW+VjSaZombnc6DORqXz7Yqg
                lyIZy77VFm5IUXcEvwdmEog1x2BAEQKgQgduDkYBWxln5U/NfVuAMVZt7h2oV+rwbO68h5
                HnY9InaEbVft2SnQmTqTawPac3nTmjZy71PdJSNgJLH9t01KVRIXLmOvaCDda1tTiILroO
                ZUdIunJJFWSdJXzLR5Z37CiG216GzK+ecMVK2QaW526j3k4TG38ECnqJ2VVIXzST66810S
                67DhJxUeXmnrJ40OFFSh+1/IKGYNqa1fV04tjOCw4DMLBsybHZU4fn9YVJK9AyHnTHxzgW
                3Lx3HJ0/hXsxnDN/LqFP4zNn2CNRXXnjRLRulQx5zm6ZQftLLFUgRIkZHysk146VV7Vf3F
                XYBUi78uygRnOia2toeTZDzg+j17+WaxotnT/oYa6EY+GnEm1YsO26mGhIhZB8s5FXMtZV
                X10ByV67VhTX6oClo4p6EW9/x6KmgNfMZY8icdA0Bbo93HPu6vZpB7mnGuurHm5nZyrhZD
                rkGB7wbwWAOFvN8t95GlTJCOUPyjLaIDYbfvmZggepBZ14DVMHf8jZYqD7ajhaKT0OPq6N
                MAAAdI3kAXZt5AF2YAAAAHc3NoLXJzYQAAAgEAyV/w/2wm+0OJ9ZHMpojex68pfnNwVDc8
                LxOZQbuOwMDT3N53F0eiWmv/ZtCfOuq6HZguqhKOOeKeCWSedCR1ikh0KCmw2MV0puoW+V
                jSaZombnc6DORqXz7YqglyIZy77VFm5IUXcEvwdmEog1x2BAEQKgQgduDkYBWxln5U/NfV
                uAMVZt7h2oV+rwbO68h5HnY9InaEbVft2SnQmTqTawPac3nTmjZy71PdJSNgJLH9t01KVR
                IXLmOvaCDda1tTiILroOZUdIunJJFWSdJXzLR5Z37CiG216GzK+ecMVK2QaW526j3k4TG3
                8ECnqJ2VVIXzST66810S67DhJxUeXmnrJ40OFFSh+1/IKGYNqa1fV04tjOCw4DMLBsybHZ
                U4fn9YVJK9AyHnTHxzgW3Lx3HJ0/hXsxnDN/LqFP4zNn2CNRXXnjRLRulQx5zm6ZQftLLF
                UgRIkZHysk146VV7Vf3FXYBUi78uygRnOia2toeTZDzg+j17+WaxotnT/oYa6EY+GnEm1Y
                sO26mGhIhZB8s5FXMtZVX10ByV67VhTX6oClo4p6EW9/x6KmgNfMZY8icdA0Bbo93HPu6v
                ZpB7mnGuurHm5nZyrhZDrkGB7wbwWAOFvN8t95GlTJCOUPyjLaIDYbfvmZggepBZ14DVMH
                f8jZYqD7ajhaKT0OPq6NMAAAADAQABAAACAApKWdFjoHZUlDc1VSTpd6DypYcttP7It82c
                DcfbIsdc0zbFM4bABV7jh/CkFo73Mb2TakcMnbH9j5/hQWuj9VG0tCLdRok9ReHFspjZXh
                9BXldkxlWkUn89germgquPC9drwntJBdKaPtZ9zokv72Py/fV3soUApwr18NZE7GjjSquV
                lMFmAFqfWcLt8SMBYpcY6bTaI5hG1wOy7FL4OFJOpxohjpuhzqvGOFXOgfo+Ej4MuBCy1P
                Zs56jFjSsQRquCLTJSstwlysvGlYc+NXhjfJS6WIyKNrKC5LhygyHMoMWSfIcp1IlhdgnT
                8/1c2CWylqUWjI0lI3Nh3Y+Wt696MwJHq0x8i3/J6Xj16Un6uL/GPtVPAq94kkebLhxrkT
                cwAdslxRlQXnAelYzTr1r586MNswximPP13hyugZiF9tcEOLag9nw3dRyuemU5c2N5r5U/
                ouUpQ+57mB/heTLVBWgFZY3mpNW3+uYOY+u1UypHSVtUDL4dPgH3An5PskWGuDw85vCoz7
                gd6PSBr5wy6YnT5ZKDBa7z6ahlcdo0eMbrTuno6CmrfnKhjvBanhsDwDPMVNtJrvly/qR+
                ZhEMF1T0efEYxM/BdIWV1WlLkh3/gfBwvOdJ7ykslGGnntf1yVff8CZ40tlwjW2VOLMbJx
                lNo/TTrdMJb6MFh8pBAAABAEKyusYaJuCblcbdQ0+C82Cu6Vbf/kpOGr+FUrk1oRrO/hrE
                aMrAfDJF+5jNeXVaLriUqnAJ7Z1lJg6O+gzRVktP1FnZCIl8u0XF9naxcMOJg0Z6MNxrXe
                5C71Txb6a4Rs7AlwUbAQ/3VdmhqmtjnOVr1RDf7Duo7F1mJ1Q2ydxgdUKx9fgLkyNnHUKc
                gqG1Q0CXRPqgg1KCpsCVU4ba+f3mdC1h06l1huFwGlHph4sxvPwcBRhaAO4IVuVpwS3vrs
                y0/cw+j/fXjo3BS+8nbqy1WtCUpRfB+jzb8ogTBfRzUKO9ghoRTHSAro3Ths17hjzwJCUq
                i14dPrL75BF8MM4AAAEBANcr109kjl3cg5jTXK6u1X6iii6c0ZiiwmO84OlgDYiKSp4AZL
                8Qj24R3+MbbL7o30nFIvMnBe/wfAo1LdIqR3iyw7XtHEn7TJfplWhah3VJo8Q4ognPAjb0
                WkIPYoq1HvnZJHCskQbtEA4ltmOZWp8rUKPnyBLo53Y3xwx40j43SNDnvKUgcna2OfhlG3
                kMyOvd6w1Up2XaCuy7EDoySm4g1WJe+1jMFKwjJPBrZr4iyxXAl5JzYp5zSoqtn1p5Ldc4
                fBOZ7/9scnEnvGkWQDbhsv3r9L/nDQrAKGXcGoyjF0t27LzYhkNTSJpS6dJQxJMGd+yScd
                NOZmqdm/SGUfMAAAEBAO+V7CDMwCW1AfNZLBQmgBjR3Glv5WmJYOe1e3dRaffqnA1LKM3E
                1IRiCa7ZYxfm6Fy3LiDHB2P3/pQ77oocusRX0InnFD9h2elXl3Gx8DxLozvToSHUsVv67G
                A3ChJRFZgL8Uxh79ma57AJQGVS3CgXYq3en8BRA0OOyZuid7abciExwSjPdaxvL+ZneYWe
                gS7f4vgMFDGuANdxWHQ1YiHOHTBGvLsZ2Gi3LJrAl7We0/zbupoPHalBN2546XQJWKPpXF
                5T4ANz9jdlP472G2+12nuNtUQYXJbCqIFp9U9ScivyryF2Iu1aSNzPzei+Vqe3cd6y3tBm
                4L8iRzER5aEAAAATZXhhbXBsZUBleGFtcGxlLmNvbQ==
                -----END OPENSSH PRIVATE KEY-----
                """
                }
        return temp_data
        # subprocess.run(["ls"])
        return "Done"

app.run(debug = True, host='0.0.0.0') 
