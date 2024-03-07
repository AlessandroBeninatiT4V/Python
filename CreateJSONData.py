import json
import numpy as np

# Generating sample data for "Sales by Product"
products = ['Ambarilla', 'Carrera', 'Montana', 'Paseo', 'Velo', 'VTT']
sales_by_product = np.random.uniform(5000000, 30000000, len(products)).tolist()

# Generating sample data for "Sales by Segment"
segments = ['Channel Partners', 'Enterprise', 'Government', 'Midmarket', 'Small Business']
sales_by_segment = np.random.uniform(1000000, 60000000, len(segments)).tolist()

# Creating JSON objects
product_data = [{"Product": prod, "Sales": sales} for prod, sales in zip(products, sales_by_product)]
segment_data = [{"Segment": seg, "Sales": sales} for seg, sales in zip(segments, sales_by_segment)]

# Convert Python dictionaries to JSON
product_json = json.dumps(product_data)
segment_json = json.dumps(segment_data)

# Save the JSON data to a file for use in Power BI
with open(r'C:\Users\AlessandroBeninati\Python\data\sales_by_product.json', 'w') as file:

    file.write(product_json)

with open(r'C:\Users\AlessandroBeninati\Python\data\sales_by_segment.json', 'w') as file:
    file.write(segment_json)
