from collections import defaultdict
from flask import render_template
from get_all_measurment_data import get_all_measurement_data
import json

def getRandomColor():
    import random
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))
def show_measurements():
    ####
    all_measurement_data = get_all_measurement_data()

    # Create a dictionary to store temperature values for each location and date
    temperature_data = defaultdict(lambda: defaultdict(list))

    # Extract data for JavaScript
    labels = sorted(list(set(measurement['timestamp'][:-9] for measurement in all_measurement_data)))
    datasets = []

    for measurement in all_measurement_data:
        location = measurement['location']
        timestamp = measurement['timestamp'][:-9]  # Remove the time part for date

        temperature_data[location][timestamp].append(measurement['temperature'])
    print(temperature_data)
    # Calculate the average temperature for each date and each location
    for location, date_temps in temperature_data.items():
        temperature_values = []
        for date, temps in date_temps.items():
            average_temp = sum(temps) / len(temps)
            temperature_values.append(average_temp)

        datasets.append({
            'label': location,
            'data': temperature_values,
            'fill': False,
            'borderColor': getRandomColor(),
            'lineTension': 0.1
        })

    # Convert data to JSON format
    print(labels)
    print('-------------------------------------------------')
    print(datasets)
    data_json = {
        'labels': labels,
        'datasets': datasets
    }
    return render_template('measurements.html', data_json=json.dumps(data_json), temps=all_measurement_data)
