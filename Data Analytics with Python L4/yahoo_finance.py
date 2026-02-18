import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Choose the stock (example: TCS on NSE)
ticker_symbol = "TCS.NS"
ticker = yf.Ticker(ticker_symbol)

# Step 2: Download 6 months of historical data
data = ticker.history(period="6mo")

# Step 3: Save to CSV
data.to_csv("tcs_history.csv")
print("Historical data saved to tcs_history.csv")

# Step 4: Load the CSV and perform analysis
df = pd.read_csv("tcs_history.csv")
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Step 5: Plot Closing price over time
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Close'], label='Closing Price')
plt.title(f"{ticker_symbol} Closing Price - Last 6 months")
plt.xlabel("Date")
plt.ylabel("Close Price (INR)")
plt.grid(True)
plt.legend()
plt.show()

# Step 6: Calculate daily returns
df['Daily Return'] = df['Close'].pct_change()

# Step 7: Plot daily returns
plt.figure(figsize=(12, 6))
df['Daily Return'].plot(kind='line')
plt.title(f"{ticker_symbol} Daily Returns - Last 6 months")
plt.xlabel("Date")
plt.ylabel("Daily Return")
plt.grid(True)
plt.show()

# Step 8: Show top 5 days with highest daily gains
print("Top 5 gain days:")
print(df.sort_values(by='Daily Return', ascending=False).head())

# Step 9: Show top 5 loss days
print("Top 5 loss days:")
print(df.sort_values(by='Daily Return').head())
