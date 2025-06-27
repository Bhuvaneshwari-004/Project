
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Load datasets with corrected file paths
orders = pd.read_csv(r"D:\Internship\project\orders.csv")
returns = pd.read_csv(r"D:\Internship\project\returns.csv")

# Merge datasets
data = orders.merge(returns, on='order_id', how='left', indicator=True)
data['returned'] = np.where(data['_merge'] == 'both', 1, 0)
data = data.drop('_merge', axis=1)

# Handle missing values
data.fillna({
    'category': 'Unknown',
    'geography': 'Unknown',
    'marketing_channel': 'Unknown',
    'price': data['price'].median()
}, inplace=True)

# Remove outliers (e.g., price > 3 standard deviations)
data = data[data['price'] <= data['price'].mean() + 3 * data['price'].std()]

# Encode categorical variables
le_category = LabelEncoder()
le_geography = LabelEncoder()
le_channel = LabelEncoder()

data['category_encoded'] = le_category.fit_transform(data['category'])
data['geography_encoded'] = le_geography.fit_transform(data['geography'])
data['marketing_channel_encoded'] = le_channel.fit_transform(data['marketing_channel'])

# Save cleaned dataset
data.to_csv(r"D:\Internship\project\cleaned_data.csv", index=False)

print("Data cleaning complete. Cleaned dataset saved as 'cleaned_data.csv'.")
