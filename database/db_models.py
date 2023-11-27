from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class measurments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.String)
    humidity = db.Column(db.String)
    created_on = db.Column(db.String)
    location = db.Column(db.String)
    date = ''
    time = ''

class users(db.Model):
    username = db.Column(db.String, primary_key=True)
    salt = db.Column(db.String)
    pwd_hash = db.Column(db.String)
