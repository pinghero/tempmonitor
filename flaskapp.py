from flask import Flask, render_template, request, g
import json
import mariadb
from datetime import datetime
import hashlib
from route_functions import *
from database.db_models import *
from flask_httpauth import HTTPBasicAuth
from hmac import compare_digest
from get_all_measurment_data import get_all_measurement_data
from show_measurments import show_measurements
import random

app = Flask(__name__,template_folder='/home/pinghero/tempmonitor/templates/')
auth = HTTPBasicAuth()

conn = mariadb.connect(host='127.0.0.1',port=3306,user='pinghero',password='Cro0asan',database='tempmonitor')
cur = conn.cursor()

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://pinghero:Cro0asan@localhost/tempmonitor'

db.init_app(app)

@auth.login_required
@app.route("/", methods=['GET'])
def show_measurements():
    return show_measurements()
#     # Use data from the database
#     all_measurement_data = get_all_measurement_data()
#
#     # Extract data for JavaScript
#     labels = sorted(list(set(measurement['timestamp'] for measurement in all_measurement_data)))
#     datasets = []
#
#     for location in set(measurement['location'] for measurement in all_measurement_data):
#         temperature_values = [measurement['temperature'] for measurement in all_measurement_data if measurement['location'] == location]
#         datasets.append({
#             'label': location,
#             'data': temperature_values,
#             'fill': False,
#             'borderColor': getRandomColor(),
#             'lineTension': 0.1
#         })
#
#     # Convert data to JSON format
#     data_json = {
#         'labels': labels,
#         'datasets': datasets
#     }
#
#     return render_template('measurements.html', data_json=json.dumps(data_json), temps=all_measurement_data)
#
# # Function to generate a random color
# def getRandomColor():
#     import random
#     return "#{:06x}".format(random.randint(0, 0xFFFFFF))

@auth.verify_password
def verify_password(username, password):
    user = users.query.filter(users.username == username).first()
    if user is not None:
        generated_hash = hashlib.sha256(user.salt.encode() + password.encode()).hexdigest()
        if compare_digest(user.pwd_hash, generated_hash):
            print("Pass is right")
            return username
    return False

@app.route("/add", methods=['POST'])
@auth.login_required
def add():
    return add_measurment(request=request)

@app.route("/new_user", methods=['POST'])
@auth.login_required
def new_user():
    return "Rejected"

if __name__ == '__main__':
    app.run(host='0.0.0.0') 
