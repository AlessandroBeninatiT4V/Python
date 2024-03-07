import json
import numpy as np

# Define products and segments
products = ['Ambarilla', 'Carrera', 'Montana', 'Paseo', 'Velo', 'VTT']
segments = ['Channel Partners', 'Enterprise', 'Government', 'Midmarket', 'Small Business']

# Generate random sales data
sales_data = []
for i in range(10):
    for product in products:
        for segment in segments:
        # Create a dictionary for each product-segment combination
         sales_data.append({
            'Product': product,
            'Segment': segment,
            'Sales': float(np.random.uniform(100000, 5000000))
        })

# Convert the list of dictionaries to a JSON string
sales_json = json.dumps(sales_data, indent=4)

# Write the JSON data to a file
with open(r'C:\Users\AlessandroBeninati\Python\data\sales_data.json', 'w') as json_file:
    json_file.write(sales_json)
