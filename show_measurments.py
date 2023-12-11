
from flask import render_template
from get_all_measurment_data import get_all_measurement_data
import json

def getRandomColor():
    import random
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))
def show_measurements():
    # Use data from the database
    all_measurement_data = get_all_measurement_data()
    measurments_by_date = []

    for measurement in all_measurement_data:
        measurments_by_date.append(set(measurement['timestamp'][:-9]))
    labels = sorted(measurments_by_date)
    # Extract data for JavaScript
    # labels = sorted(list(set(measurement['timestamp'] for measurement in all_measurement_data)))
    datasets = []

    for location in set(measurement['location'] for measurement in all_measurement_data):
        temperature_values = [measurement['temperature'] for measurement in all_measurement_data if measurement['location'] == location]
        datasets.append({
            'label': location,
            'data': temperature_values,
            'fill': False,
            'borderColor': getRandomColor(),
            'lineTension': 0.1
        })

    # Convert data to JSON format
    data_json = {
        'labels': labels,
        'datasets': datasets
    }

    return render_template('measurements.html', data_json=json.dumps(data_json), temps=all_measurement_data)