📈 Coca-Cola Stock Analysis
A comprehensive time-series analysis project leveraging over a century of historical trading data from Coca-Cola (KO). This project explores trends, volatility, volume patterns, and predictive modeling based on stock market behaviors.

📂 Project Structure
bash
Copy
Edit
coca-cola-stock-analysis/
│
├── data/                # Original dataset (.csv) and cleaned version
├── notebooks/           # Jupyter notebooks for exploration, analysis, and modeling
├── scripts/             # Python scripts for data cleaning and automation
├── README.md            # Project documentation
├── requirements.txt     # Project dependencies
└── .gitignore
🔍 Project Objectives
Ingest and preprocess over 100 years of KO stock data.

Perform exploratory data analysis (EDA) with descriptive statistics and plots.

Handle missing values, datetime parsing, and data cleaning.

Visualize price movements, volume trends, and rolling averages.

Engineer financial features (e.g., moving averages, price deltas).

Apply and evaluate predictive models (linear regression, time series).

Build reusable scripts for data cleaning and visualization.

⚙️ Data Processing & Analysis Techniques
Datetime conversion for proper time indexing.

Null value detection and removal to ensure modeling accuracy.

Descriptive statistics: mean, std dev, min/max, percentiles.

Price visualization: daily closing, adjusted close, open/high/low patterns.

Volume tracking: trade activity over decades.

Rolling statistics: moving averages (e.g., 50-day, 200-day).

Log returns and volatility: foundational analysis for financial modeling.

Simple predictive modeling: linear regression for price forecasting.

📊 Dataset Information
Source: Kaggle

Coverage: 1919 – 2025 (daily frequency)

Columns:

date: Trade date

open: Opening price

high: High of day

low: Low of day

close: Closing price

adj_close: Adjusted closing price for splits/dividends

volume: Number of shares traded

📦 Requirements
bash
Copy
Edit
pandas
matplotlib
seaborn
plotly
scikit-learn
Install with:

bash
Copy
Edit
pip install -r requirements.txt
