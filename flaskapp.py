from flask import Flask, render_template, request, g
import json
import mariadb
from datetime import datetime
from verify_password import verify_password
from route_functions import *
from database.db_models import measurments, users
from flask_httpauth import HTTPBasicAuth
from dao import get_all_measurement_data
import random

app = Flask(__name__,template_folder='/home/pinghero/tempmonitor/templates/')
auth = HTTPBasicAuth()

conn = mariadb.connect(host='127.0.0.1',port=3306,user='pinghero',password='Cro0asan',database='tempmonitor')
cur = conn.cursor()

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://pinghero:Cro0asan@localhost/tempmonitor'

db.init_app(app)

@auth.verify_password
def password_check(username, password):
    return verify_password(username, password)

@app.route("/", methods=['GET'])
@auth.login_required
def index():
    return show_measurements()

@app.route("/get_table_data", methods=['GET'])
def update_data():
    return get_all_measurement_data()

@app.route("/get_filtered_table_data", methods=['GET'])
def update_filtered_data():
    filtered_data = request.get_json()
    return get_filtered_data(filtered_data)

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
