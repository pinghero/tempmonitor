from collections import defaultdict

# Help function to generate random color for different location representation
def get_random_color():
    import random
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

# Calculates the average temperature for the last 10 days present in the database
# and converts the data to datasets (temp, location and chart color) and labels (datetime)
def convert_graph_data(all_measurement_data):
    # Create a dictionary to store temperature values for each location and date
    temperature_data = defaultdict(lambda: defaultdict(list))

    # Extract data for JavaScript
    labels = sorted(list(set(measurement['timestamp'][:-9] for measurement in all_measurement_data)))
    datasets = []

    for measurement in all_measurement_data:
        location = measurement['location']
        timestamp = measurement['timestamp'][:-9]  # Remove the time part for date
        temperature_data[location][timestamp].append(measurement['temperature'])

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
            'borderColor': get_random_color(),
            'lineTension': 0.1
        })

    # Convert data to JSON format
    data_json = {
        'labels': labels,
        'datasets': datasets
    }

    return data_json
