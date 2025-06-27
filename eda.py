
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define directory
data_dir = r"D:\Internship\project"

# Load cleaned data
data = pd.read_csv(os.path.join(data_dir, 'cleaned_data.csv'))

# Calculate return rates
return_rates = data.groupby(['category', 'geography', 'marketing_channel'])['returned'].mean().reset_index()
return_rates.rename(columns={'returned': 'return_rate'}, inplace=True)

# Visualize return rates by category
plt.figure(figsize=(10, 6))
sns.barplot(data=return_rates, x='category', y='return_rate')
plt.title('Return Rate by Product Category')
plt.xticks(rotation=45)
plt.savefig(os.path.join(data_dir, 'return_rate_category.png'))

# Visualize return rates by geography
plt.figure(figsize=(10, 6))
sns.barplot(data=return_rates, x='geography', y='return_rate')
plt.title('Return Rate by Geography')
plt.xticks(rotation=45)
plt.savefig(os.path.join(data_dir, 'return_rate_geography.png'))

# Visualize return rates by marketing channel
plt.figure(figsize=(10, 6))
sns.barplot(data=return_rates, x='marketing_channel', y='return_rate')
plt.title('Return Rate by Marketing Channel')
plt.xticks(rotation=45)
plt.savefig(os.path.join(data_dir, 'return_rate_channel.png'))

# Save return rates to CSV for Power BI
return_rates.to_csv(os.path.join(data_dir, 'return_rates.csv'), index=False)

print(f"EDA complete. Visualizations and return rates saved in: {data_dir}")
