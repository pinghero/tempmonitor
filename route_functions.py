from database.db_models import *
from flask import Flask, render_template, request, url_for, redirect, g
from dao import get_all_measurement_data, get_filtered_data
from convert_graph_data import convert_graph_data
import json
import os
import mariadb
from datetime import datetime
import hashlib
import os
import uuid

def show_measurements():
    # Get all measurements
    all_measurement_data = get_all_measurement_data()

    # Convert measurements to labels and datasets for graph rendering
    data_json = convert_graph_data(all_measurement_data)

    return render_template('measurements.html', data_json=json.dumps(data_json), temps=all_measurement_data)
def filter_data():
    filters = request.get_json()
    filtered_data = get_filtered_data(filters)

    return filtered_data

def add_measurment(request):
    try:
        json_string = request.get_json(force=True)
        new_data = measurments(temperature=json_string['temperature'], humidity=json_string['humidity'])
        db.session.add(new_data)
        db.session.commit()
        return 'Success!', 200
    except:
        return "BAD REQUEST", 400

def add_new_user(request):
    json_string = request.get_json(force=True)
    generated_salt = uuid.uuid4().hex
    generated_hash = hashlib.sha256(generated_salt.encode() + json_string['password'].encode()).hexdigest()
    new_data = users(username=json_string['username'], salt=generated_salt, pwd_hash=generated_hash)
    db.session.add(new_data)
    db.session.commit()
    return 'YES'

def log_in(request):
    json_string = request.get_json(force=True)
    user = users.query.filter(users.username == json_string['username']).first()
    if user is not None:
        if user.pwd_hash is not None:
            return 'did it'
    else:
        return 'No user'

