import pandas as pd
import numpy as np
import random

# Define the number of entries we want
num_entries = 1000

# Example data to populate the CSV
countries = ['Country A', 'Country B', 'Country C']
regions = ['Region 1', 'Region 2', 'Region 3']
cities = ['City X', 'City Y', 'City Z']
years = list(range(2018, 2023))

# Create empty dataframe
data = pd.DataFrame({
    'Country': np.random.choice(countries, num_entries),
    'Region': np.random.choice(regions, num_entries),
    'City': np.random.choice(cities, num_entries),
    'Financial_Year': np.random.choice(years, num_entries),
    'Amount': np.random.uniform(10000, 100000, num_entries).round(2)  # random financial amounts
})

# Save dataframe to a CSV file
csv_file_path = r'C:\Users\AlessandroBeninati\Python\FinancialDemo\financial_data.csv'
data.to_csv(csv_file_path, index=False)
