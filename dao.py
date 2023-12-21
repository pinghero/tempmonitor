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

    if 'tempFrom' in filter_dict:
        query = query.filter(measurments.temperature >= filter_dict['tempFrom'])

    if 'tempTo' in filter_dict:
        query = query.filter(measurments.temperature <= filter_dict['tempTo'])

    if 'humidityFrom' in filter_dict:
        query = query.filter(measurments.humidity >= filter_dict['humidityFrom'])

    if 'humidityTo' in filter_dict:
        query = query.filter(measurments.humidity <= filter_dict['humidityTo'])

    if 'dateFrom' in filter_dict:
        query = query.filter(measurments.created_on >= filter_dict['dateFrom'])

    if 'dateTo' in filter_dict:
        query = query.filter(measurments.created_on <= filter_dict['dateTo'])

    if 'location' in filter_dict:
        query = query.filter(measurments.location == filter_dict['location'])

    print(query)
    print(measurments)
    measurements = query.all()

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



