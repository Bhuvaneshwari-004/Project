
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib
import os


data_dir = r"D:\Internship\project"

data = pd.read_csv(os.path.join(data_dir, 'cleaned_data.csv'))

features = ['category_encoded', 'geography_encoded', 'marketing_channel_encoded', 'price']
X = data[features]
y = data['returned']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

data['return_probability'] = model.predict_proba(X)[:, 1]

print("Model Performance:")
print(classification_report(y_test, model.predict(X_test)))


joblib.dump(model, os.path.join(data_dir, 'return_prediction_model.pkl'))


data.to_csv(os.path.join(data_dir, 'data_with_predictions.csv'), index=False)

print(f"Logistic regression model trained and saved. Dataset with predictions saved in: {data_dir}")
