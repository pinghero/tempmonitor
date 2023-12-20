from database.db_models import *
from flask import Flask, render_template, request, url_for, redirect, g
import json
import os
import mariadb
from datetime import datetime
import hashlib
import os
import uuid

#def show_measurments(request):
#    rows = measurments.query.all()
#    rows_to_show = []
#    for row in rows:
#        row.date = row.created_on.date()
#        row.time = row.created_on.time()
#    return render_template('measurements.html', temps=rows)

def filter_data():
    filters = request.get_json()
    print(filters)
def get_all_measurement_data():
    measurements_data = measurments.query.all()

    data = []

    for measurement in measurements_data:
        timestamp = measurement.created_on.strftime("%Y-%m-%d %H:%M:%S")
        data.append({
            'location': measurement.location,
            'temperature': float(measurement.temperature),
            'humidity': float(measurement.humidity),
            'timestamp': timestamp
        })

    return data

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

