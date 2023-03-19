from flask import Flask
from flask import request
from flask_cors import CORS
import subprocess


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
    
    subprocess.call('cd ' + platform + ' && terraform apply -auto-approve', shell=True)
    # result = subprocess.check_output('cd ' + platform + ' && terraform apply -auto-approve', shell=True)
    subprocess.call('cd ' + platform + ' && terraform output', shell=True)
    # print(result)
    print('CHECK THE OUTPUT NOW----------------------')
    subprocess.call('cd ' + platform + ' && terraform output instance_public_ip > terraform_output', shell=True)
    #subprocess.call('export MY_OUTPUT_VARIABLE=$(terraform output instance_public_ip)', shell=True)
    #subprocess.call('echo $MY_OUTPUT_VARIABLE', shell=True)
    # print(result)
    f = open("aws/terraform_output", "r")
    tempData = f.read()
    print('tempData')
    print(tempData[1:-2])
    print('ENDDDDDDDDDDDDDDDDDDDDDDd')
    temp_data = {"result": tempData[1:-2]}
    return temp_data
    # subprocess.run(["ls"])
    return "Done"

app.run(debug = True, host='0.0.0.0') 
