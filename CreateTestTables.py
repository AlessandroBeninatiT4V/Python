# Let's create a CSV file with sales data (fact table) and some dimension tables

import pandas as pd
from datetime import datetime, timedelta
import random

# Creating a Sales Fact Table
sales_data = {
    'SaleID': range(1, 101),
    'ProductID': [random.randint(1, 10) for _ in range(100)],
    'CustomerID': [random.randint(1, 20) for _ in range(100)],
    'SaleDate': [(datetime(2023, 1, 1) + timedelta(days=random.randint(0, 364))).strftime('%Y-%m-%d') for _ in range(100)],
    'Quantity': [random.randint(1, 5) for _ in range(100)],
    'SaleAmount': [random.uniform(20.0, 500.0) for _ in range(100)]
}
sales_df = pd.DataFrame(sales_data)
sales_df['SaleAmount'] = sales_df['SaleAmount'].round(2)

# Creating Product Dimension Table
product_data = {
    'ProductID': range(1, 11),
    'ProductName': [f'Product {chr(65+i)}' for i in range(10)],
    'Category': [random.choice(['Electronics', 'Clothing', 'Home & Kitchen']) for _ in range(10)]
}
product_df = pd.DataFrame(product_data)

# Creating Customer Dimension Table
customer_data = {
    'CustomerID': range(1, 21),
    'CustomerName': [f'Customer {i}' for i in range(1, 21)],
    'Location': [random.choice(['New York', 'California', 'Texas', 'Florida', 'Illinois']) for _ in range(20)]
}
customer_df = pd.DataFrame(customer_data)

# Saving to CSV files
sales_df.to_csv('C:/Users/AlessandroBeninati/Python/sales_data.csv', index=False)
product_df.to_csv('C:/Users/AlessandroBeninati/Python/product_dimension.csv', index=False)
customer_df.to_csv('C:/Users/AlessandroBeninati/Python/customer_dimension.csv', index=False)
