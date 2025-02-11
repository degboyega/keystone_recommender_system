import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

# Define possible banking products
banking_products = ["Savings Account", "Current Account", "Credit Card", "Personal Loan", 
                    "Mortgage Loan", "Fixed Deposit", "Mutual Fund", "Car Loan"]

# Generate synthetic customer transactions
num_customers = 1000  # Simulating 1000 customers
num_transactions = 10000  # Simulating 10000 transactions

data = []
for _ in range(num_transactions):
    customer_id = np.random.randint(1000, 2000)  # Unique customer IDs
    transaction_date = fake.date_between(start_date="-2y", end_date="today")
    product_used = np.random.choice(banking_products)
    transaction_amount = round(np.random.uniform(500, 100000), 2)  # Random amount
    tenure_years = np.random.randint(1, 15)  # How long customer has been with bank
    transaction_frequency = np.random.randint(1, 50)  # Monthly transaction count

    data.append([customer_id, transaction_date, product_used, transaction_amount, tenure_years, transaction_frequency])

# Create DataFrame
df = pd.DataFrame(data, columns=["customer_id", "transaction_date", "product_used", 
                                 "transaction_amount", "customer_tenure", "transaction_frequency"])

# Save dataset as CSV
df.to_csv("../data/raw/synthetic_banking_transactions.csv", index=False)

print("✅ Synthetic banking dataset created!")
print(df.head())
