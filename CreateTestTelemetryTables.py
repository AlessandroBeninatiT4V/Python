import pandas as pd
from datetime import datetime, timedelta
import random

# Create a function to generate dummy data
def create_dummy_data(num_records):
    # Create a date range
    start_date = datetime.now() - timedelta(days=365) # start date set to one year ago
    date_range = [start_date + timedelta(days=x) for x in range(num_records)]
    
    # Create device types
    device_types = ['Sensor', 'Camera', 'Thermostat', 'Light']
    
    # Create reading types
    reading_types = ['Temperature', 'Humidity', 'Light', 'Motion']
    
    # Generate dummy data
    data = {
        'datetime': [random.choice(date_range) for _ in range(num_records)],
        'deviceid': [random.randint(1000, 9999) for _ in range(num_records)],
        'devicetype': [random.choice(device_types) for _ in range(num_records)],
        'readingtype': [random.choice(reading_types) for _ in range(num_records)],
        'readingvalue': [round(random.uniform(10.5, 99.9), 2) for _ in range(num_records)]
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Sort the DataFrame by datetime
    df.sort_values('datetime', inplace=True)
    
    # Return the DataFrame
    return df

# Generate dummy data for 100 records as an example
dummy_data_df = create_dummy_data(1000)

# Save the DataFrame to a CSV file
dummy_data_file = 'C:/Users/AlessandroBeninati/Python/telemetry_dummy_data.csv'
dummy_data_df.to_csv(dummy_data_file, index=False)
