from collections import defaultdict
from flask import render_template
from dao import get_all_measurement_data
from convert_graph_data import convert_graph_data
import json
def show_measurements():
    # Get all measurements
    all_measurement_data = get_all_measurement_data()

    # Convert measurements to labels and datasets for graph rendering
    data_json = convert_graph_data(all_measurement_data)

    return render_template('measurements.html', data_json=json.dumps(data_json), temps=all_measurement_data)

def show_filtered_measurements():
# implement later
    return None
