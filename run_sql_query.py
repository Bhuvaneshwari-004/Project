
import pandas as pd
import sqlite3
import os

# Define directory
data_dir = r"D:\Internship\project"
db_path = os.path.join(data_dir, 'ecommerce.db')

# Connect to SQLite database
conn = sqlite3.connect(db_path)

# Define SQL query
query = """
SELECT 
    p.product_id,
    p.category,
    p.geography,
    p.marketing_channel,
    AVG(p.return_probability) AS return_risk_score,
    COUNT(*) AS total_orders,
    SUM(p.returned) AS total_returns,
    AVG(p.returned) AS return_rate
FROM 
    data_with_predictions p
GROUP BY 
    p.product_id,
    p.category,
    p.geography,
    p.marketing_channel;
"""

# Execute query and save results
dashboard_data = pd.read_sql_query(query, conn)
dashboard_data.to_csv(os.path.join(data_dir, 'dashboard_data.csv'), index=False)

# Close connection
conn.close()

print(f"SQL query results saved as 'dashboard_data.csv' in: {data_dir}")
