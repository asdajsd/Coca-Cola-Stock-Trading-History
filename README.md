
---

## 🔍 Project Objectives

- Preprocess and clean KO stock data from 1919 to 2025.
- Perform exploratory data analysis (EDA) with statistical summaries.
- Visualize trends in prices, volumes, and volatility.
- Engineer features such as rolling averages and log returns.
- Build regression-based models for stock price prediction.
- Develop reusable scripts for automation and reproducibility.

---

## ⚙️ Techniques Used

- Datetime parsing for time-indexed analysis
- Handling missing values to ensure data quality
- Descriptive statistics: mean, std, min, max, quartiles
- Visualization:
  - Price (Open, High, Low, Close, Adj Close)
  - Trading volume trends
  - Moving averages (e.g., 50-day, 200-day)
- Volatility metrics: daily returns and log return analysis
- Predictive modeling using linear regression on time series

---

## 📊 Dataset Information

- **Source**: [Kaggle – Coca-Cola Stock Data (1919–2025)](https://www.kaggle.com/datasets/muhammadatiflatif/coca-cola-stock-data-over-100-years-of-trading)
- **Frequency**: Daily trading data

**Columns**:
- `date`: Trade date
- `open`: Opening price
- `high`: Highest price of the day
- `low`: Lowest price of the day
- `close`: Closing price
- `adj_close`: Adjusted close (for dividends & splits)
- `volume`: Shares traded

---

## 📦 Installation & Requirements

Install the required Python libraries:

```bash
pip install -r requirements.txt

Dependencies:

pandas

matplotlib

seaborn

plotly

scikit-learn
