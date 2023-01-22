from flask import Flask
from flask import request
from flask_cors import CORS
import subprocess


app = Flask(__name__)
CORS(app)

@app.route("/")
def start():
    return "<p>Hello, Tasty World!</p>"

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
