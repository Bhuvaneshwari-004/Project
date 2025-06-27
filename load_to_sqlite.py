
import pandas as pd
import sqlite3
import os

# Define directory
data_dir = r"D:\Internship\project"

# Connect to SQLite database
db_path = os.path.join(data_dir, 'ecommerce.db')
conn = sqlite3.connect(db_path)

# Load data_with_predictions.csv
data = pd.read_csv(os.path.join(data_dir, 'data_with_predictions.csv'))

# Write to SQLite database
data.to_sql('data_with_predictions', conn, if_exists='replace', index=False)

# Verify table creation
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables in database:", cursor.fetchall())

# Close connection
conn.close()

print(f"Data loaded into SQLite database: {db_path}")
