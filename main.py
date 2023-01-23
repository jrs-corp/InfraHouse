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
    print(platform, codelocation)
    subprocess.run(["pwd"])
    # subprocess.Popen("ls", cwd="/")
    # subprocess.run(["terraform init"], shell=True)
    subprocess.call('cd ' + platform + ' && terraform init', shell=True)
    subprocess.call('cd ' + platform + ' && terraform plan', shell=True)
    subprocess.call('cd ' + platform + ' && terraform apply -auto-approve', shell=True)
    # subprocess.run(["ls"])
    return "Done"

app.run(debug = True, host='0.0.0.0') 
