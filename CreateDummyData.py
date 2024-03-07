import pandas as pd
import numpy as np

# Function to create dummy data based on the given schema in the image
def create_dummy_data():
    # Set the seed for reproducibility
    np.random.seed(0)

    # Creating dummy data for Customers
    customers = pd.DataFrame({
        'Customer ID': np.arange(1, 11),
        'Customer Name': [f'Customer{i}' for i in range(1, 11)],
        'ZIP Code': np.random.randint(10000, 99999, size=(10)).astype(str)
    })

    # Creating dummy data for Products
    products = pd.DataFrame({
        'Product ID': np.arange(1, 21),
        'Product Name': [f'Product{i}' for i in range(1, 21)]
    })

    # Creating dummy data for Baskets
    baskets = pd.DataFrame({
        'Basket ID': np.arange(1, 16),
        'Purchase Date': pd.date_range(start='2023-01-01', periods=15, freq='D'),
        'Customer ID': np.random.choice(customers['Customer ID'], 15),
        'Total Amount': np.random.uniform(50, 500, size=(15)).round(2)
    })

    # Creating dummy data for Basket Items
    basket_items = pd.DataFrame({
        'Basket ID': np.repeat(baskets['Basket ID'], 3),
        'Product ID': np.random.choice(products['Product ID'], 45),
        'Amount': np.random.uniform(5, 100, size=(45)).round(2)
    })

    return customers, products, baskets, basket_items

# Generate the dummy data
customers_dummy, products_dummy, baskets_dummy, basket_items_dummy = create_dummy_data()

# Show the dummy dataframes
customers_dummy.to_csv('C:/Users/AlessandroBeninati/Python/dummy_data/customers_dummy.csv', index=False)
products_dummy.to_csv('C:/Users/AlessandroBeninati/Python/dummy_data/products_dummy.csv', index=False)
baskets_dummy.to_csv('C:/Users/AlessandroBeninati/Python/dummy_data/baskets_dummy.csv', index=False)
basket_items_dummy.to_csv('C:/Users/AlessandroBeninati/Python/dummy_data/basket_items_dummy.csv', index=False)
print("Done")