from database.db_models import measurments

# Queries all measurement data in database and returns them as a list of dictionaries
def get_all_measurement_data():
    measurements = measurments.query.all()
    data = []

    for measurement in measurements:
        timestamp = measurement.created_on.strftime("%Y-%m-%d %H:%M:%S")  # Convert datetime to string

        data.append({
            'location': measurement.location,
            'temperature': float(measurement.temperature),
            'humidity': float(measurement.humidity),
            'timestamp': timestamp
        })

    return data
def get_filtered_data():

    return None