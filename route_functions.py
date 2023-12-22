from database.db_models import *
from flask import Flask, render_template, request, url_for, redirect, g, jsonify
from dao import *
from convert_graph_data import convert_graph_data
import json
import mariadb
import hashlib
import uuid

def show_measurements():
    # Get all measurements
    all_measurement_data = get_all_measurement_data()

    # Convert measurements to labels and datasets for graph rendering
    data_json = convert_graph_data(all_measurement_data)

    return render_template('measurements.html', data_json=json.dumps(data_json), data=all_measurement_data)

def filter_data():
    filters = request.get_json()
    filtered_data = get_filtered_data(filters)

    return filtered_data

def add_measurment(request):

 #   try:

    # Convert JSON to measurements database model
    json_string = request.get_json(force=True)
    new_data = measurments(temperature=json_string['temperature'],
                           humidity=json_string['humidity'],
                           location=json_string['location'])

    # Add new data to database
    db.session.add(new_data)
    db.session.commit()
    return 'Success!', 200

 #   except:

#      return "BAD REQUEST", 400

# Adds new user
def add_new_user(request):
    json_string = request.get_json(force=True)

    # Generate random password salt
    generated_salt = uuid.uuid4().hex

    # Generate hash using password and generated salt
    generated_hash = hashlib.sha256(generated_salt.encode() + json_string['password'].encode()).hexdigest()

    # Convert data to users database model
    new_data = users(username=json_string['username'], salt=generated_salt, pwd_hash=generated_hash)

    # Add new user to database
    db.session.add(new_data)
    db.session.commit()
