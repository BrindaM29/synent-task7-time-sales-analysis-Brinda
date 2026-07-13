# ==============================
# STOCK PRICE TIME SERIES ANALYSIS
# ==============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

# ------------------------------
# Load Dataset
# ------------------------------

df = pd.read_csv("stock_data.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

# ------------------------------
# Data Preprocessing
# ------------------------------

df['Date'] = pd.to_datetime(df['Date'])

df = df.sort_values('Date')

df = df.dropna()

print("\nMissing Values:")
print(df.isnull().sum())

# ------------------------------
# Trend Analysis
# ------------------------------

plt.figure(figsize=(12,6))
plt.plot(df['Date'], df['Close'])
plt.title("Stock Closing Price Trend")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.grid(True)

plt.savefig("trend_analysis.png")
plt.show()

# ------------------------------
# Moving Average Analysis
# ------------------------------

df['MA30'] = df['Close'].rolling(window=30).mean()

plt.figure(figsize=(12,6))
plt.plot(df['Date'], df['Close'], label='Close Price')
plt.plot(df['Date'], df['MA30'], label='30-Day Moving Average')

plt.title("30-Day Moving Average")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)

plt.savefig("moving_average.png")
plt.show()

# ------------------------------
# Daily Return Analysis
# ------------------------------

df['Daily_Return'] = df['Close'].pct_change()

plt.figure(figsize=(12,6))
plt.plot(df['Date'], df['Daily_Return'])

plt.title("Daily Returns")
plt.xlabel("Date")
plt.ylabel("Return")
plt.grid(True)

plt.savefig("daily_returns.png")
plt.show()

# ------------------------------
# Volume Analysis
# ------------------------------

plt.figure(figsize=(12,6))
plt.plot(df['Date'], df['Volume'])

plt.title("Trading Volume Over Time")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.grid(True)

plt.savefig("volume_analysis.png")
plt.show()

# ------------------------------
# Correlation Heatmap
# ------------------------------

plt.figure(figsize=(8,6))

sns.heatmap(
    df[['Open','High','Low','Close','Volume']].corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")

plt.savefig("correlation_heatmap.png")
plt.show()

# ------------------------------
# Seasonality Detection
# ------------------------------

print("\nGenerating Seasonal Decomposition...")

result = seasonal_decompose(
    df['Close'],
    model='additive',
    period=30
)

result.plot()

plt.savefig("seasonality_analysis.png")
plt.show()

# ------------------------------
# Business Insights
# ------------------------------

print("\n==============================")
print("TIME SERIES INSIGHTS")
print("==============================")

print("\nHighest Closing Price:")
print(df['Close'].max())

print("\nLowest Closing Price:")
print(df['Close'].min())

print("\nAverage Closing Price:")
print(round(df['Close'].mean(), 2))

print("\nHighest Trading Volume:")
print(df['Volume'].max())

print("\nAverage Daily Return:")
print(round(df['Daily_Return'].mean(), 4))

print("\nProject Completed Successfully!")
print("Graphs Saved:")
print("1. trend_analysis.png")
print("2. moving_average.png")
print("3. daily_returns.png")
print("4. volume_analysis.png")
print("5. correlation_heatmap.png")
print("6. seasonality_analysis.png")
