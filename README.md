# E-Commerce Return Rate Reduction Analysis

This project analyzes e-commerce return rates to identify high-risk products and trends, enabling data-driven strategies to reduce returns. It uses synthetic order and return data, processed through a Python-based pipeline, stored in SQLite, and visualized in an interactive Power BI.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Tools Used](#tools-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Results](#results)
- [Future Improvements](#future-improvements)


## Project Overview
High return rates in e-commerce impact profitability and efficiency. This project generates synthetic order and return data, preprocesses it, applies logistic regression to predict return probabilities, stores results in an SQLite database, and visualizes insights in Power BI. The dashboard includes creative visuals like treemaps, heatmaps, scatter plots, donut charts, and gauges, with interactive slicers and drill-throughs.

## Features
- Synthetic data generation for 10,000 orders with 15% returns.
- Logistic regression model to predict return probabilities.
- SQLite database for efficient data storage and querying.
- Interactive Power BI dashboard with visuals for return rates and risk scores by category, geography, and marketing channel.
- PDF report summarizing the project and findings.

## Tools Used
- **Python**: Data generation, preprocessing, and modeling (pandas, NumPy, scikit-learn).
- **SQLite**: Data storage and SQL queries.
- **Power BI Desktop**: Interactive visualizations.
- **Command Prompt (CMD)**: Script execution.


## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/ecommerce-return-rate-analysis.git
   cd ecommerce-return-rate-analysis


Install Python Dependencies:
pip install pandas numpy scikit-learn


Install Power BI Desktop:

Download from https://powerbi.microsoft.com/desktop/.


Usage

Generate Data:
cd scripts
python generate_dataset.py
python preprocessing.py
python logistic_regression.py

Outputs: data/orders.csv, data/returns.csv, data/cleaned_data.csv, data/data_with_predictions.csv.

Load Data to SQLite:
python load_to_sqlite.py

Output: data/ecommerce.db.

Run SQL Queries:
python run_sql_query.py

Output: data/dashboard_data.csv.

Project Structure
ecommerce-return-rate-analysis/
├── scripts/
│   ├── generate_dataset.py
│   ├── preprocessing.py
│   ├── logistic_regression.py
│   ├── load_to_sqlite.py
│   ├── run_sql_query.py
├── data/
│   ├── orders.csv
│   ├── returns.csv
│   ├── cleaned_data.csv
│   ├── data_with_predictions.csv
│   ├── dashboard_data.csv
│   ├── ecommerce.db
├── reports/
│   ├── return_risk_dashboard.pbix
│   ├── project_report.tex
│   ├── project_report.pdf

Results

Identified high return rates in categories like Clothing (e.g., 25%) and marketing channels like Social Media (e.g., 40% of returns).
Power BI dashboard provides interactive visuals (treemaps, heatmaps, scatter plots) to explore trends.
PDF report summarizes methodology and findings.

Future Improvements

Integrate real-time data feeds.
Use advanced machine learning models (e.g., XGBoost) for better predictions.
Automate data refresh in Power BI Service.
![{BE4910B9-9139-4869-8F40-291ADF708DB9}](https://github.com/user-attachments/assets/e698850d-70ac-4a37-97fd-36568bfefa49)

