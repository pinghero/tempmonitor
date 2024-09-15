from flask import Flask, render_template, request, g
import json
import mariadb
from datetime import datetime
from verify_password import verify_password
from route_functions import show_measurements, get_all_measurement_data, get_filtered_data, add_measurment
from database.db_models import *
from flask_httpauth import HTTPBasicAuth
from dao import get_all_measurement_data
from blockchain import announce, get_peers

# Template configuration
app = Flask(__name__, template_folder='/home/pinghero/tempmonitor/templates/')

# Basic auth initialization
auth = HTTPBasicAuth()

# Database initialization
conn = mariadb.connect(host='127.0.0.1', port=3306, user='pinghero',
                       password='Cro0asan', database='tempmonitor')
cur = conn.cursor()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://pinghero:Cro0asan@localhost/tempmonitor'
db.init_app(app)

# Verification decorator


@auth.verify_password
def password_check(username, password):
    return verify_password(username, password)

# Index route


@app.route("/", methods=['GET'])
@auth.login_required
def index():
    return show_measurements()

# Data table for index page (all measurements)


@app.route("/get_table_data", methods=['GET'])
def update_data():
    return get_all_measurement_data()

# Data table with filtered data


@app.route("/get_filtered_table_data", methods=['POST'])
def update_filtered_data():
    filtered_data = request.get_json()
    return get_filtered_data(filtered_data)

# ESP controller route to add measurement


@app.route("/add", methods=['POST'])
@auth.login_required
def add():
    return add_measurment(request=request)


@app.route("/announce", methods=['POST'])
@auth.login_required
def announce():
    return announce()


@app.route("/peers", methods=['GET'])
@auth.login_required
def get_peers():
    return get_peers()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
