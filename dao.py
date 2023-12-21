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
from flask import jsonify

def get_filtered_data(filters):
    filter_dict = {k: v for k, v in filters.items() if v is not None}
    query = measurments.query

    if not filter_dict['tempFrom'].isEmpty():
        query = query.filter(measurments.temperature >= filter_dict['tempFrom'])

    if not filter_dict['tempTo'].isEmpty():
        query = query.filter(measurments.temperature <= filter_dict['tempTo'])

    if not filter_dict['humidityFrom'].isEmpty():
        query = query.filter(measurments.humidity >= filter_dict['humidityFrom'])

    if not filter_dict['humidityTo'].isEmpty():
        query = query.filter(measurments.humidity <= filter_dict['humidityTo'])

    if not filter_dict['dateFrom'].isEmpty():
        query = query.filter(measurments.created_on >= filter_dict['dateFrom'])

    if not filter_dict['dateTo'].isEmpty():
        query = query.filter(measurments.created_on <= filter_dict['dateTo'])

    if not filter_dict['location'].isEmpty():
        query = query.filter(measurments.location == filter_dict['location'])

    print(query)
    measurements = query.all()
    print(measurments)

    data = []

    for measurement in measurements:
        timestamp = measurement.created_on.strftime("%Y-%m-%d %H:%M:%S")  # Convert datetime to string
        data.append({
            'timestamp': timestamp,
            'location': measurement.location,
            'temperature': float(measurement.temperature),
            'humidity': float(measurement.humidity)
        })

    return jsonify(data)



