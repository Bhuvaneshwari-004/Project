import pandas as pd
import os

# Define directory
data_dir = r"D:\Internship\project"

# Load data with predictions
data = pd.read_csv(os.path.join(data_dir, 'data_with_predictions.csv'))

# Filter high-risk products
high_risk = data[data['return_probability'] > 0.7][['product_id', 'category', 'geography', 'marketing_channel', 'return_probability']]

# Save to CSV
high_risk.to_csv(os.path.join(data_dir, 'high_risk_products.csv'), index=False)

print(f"High-risk products saved as 'high_risk_products.csv' in: {data_dir}")
