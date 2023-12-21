from database.db_models import measurments
from flask import jsonify
# Queries all measurement data in database and returns them as a list of dictionaries
def get_all_measurement_data():
    measurements = measurments.query.all()
    data = []

    for measurement in measurements:
        timestamp = measurement.created_on.strftime("%Y-%m-%d %H:%M:%S")  # Convert datetime to string

        data.append({
            'timestamp': timestamp,
            'location': measurement.location,
            'temperature': float(measurement.temperature),
            'humidity': float(measurement.humidity)
        })

    return data
def get_filtered_data(filters):
    # Remove keys with None value
    filter_dict = {k: v for k, v in filters.items() if v is not None}

    measurements = measurments.query.filter(measurments.temperature >= filter_dict['tempFrom']).all()
    print(measurements)
    data =[]

    for measurement in measurements:
        timestamp = measurement.created_on.strftime("%Y-%m-%d %H:%M:%S")  # Convert datetime to string
        data.append({
            'location': measurement.location,
            'temperature': float(measurement.temperature),
            'humidity': float(measurement.humidity),
            'timestamp': timestamp
        })

    return jsonify(data)


