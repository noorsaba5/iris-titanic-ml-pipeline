# Essential Imports for Data Operations

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
from statsmodels.tsa.arima.model import ARIMA


# Retrieve Stock and Cryptocurrency Information

def get_stock_prices(symbols, duration="6mo"):
    dataset = yf.download(symbols, period=duration, group_by='ticker', auto_adjust=True)
    return dataset

def stock_snapshot(symbol):
    asset = yf.Ticker(symbol)
    print(f"\nDetails for: {symbol}")
    print("Market Capitalization:", asset.info.get("marketCap", "Unavailable"))
    print("Trailing P/E Ratio:", asset.info.get("trailingPE", "Unavailable"))
    print("Yield (Dividend):", asset.info.get("dividendYield", "Unavailable"))
    print("Dividend History:\n", asset.dividends.tail())
    print("Stock Splits:\n", asset.splits.tail())
    print("Income Statement:\n", asset.financials.head())
    print("Balance Sheet:\n", asset.balance_sheet.head())
    print("Cash Flow Summary:\n", asset.cashflow.head())
    print("Latest Analyst Opinions:\n", asset.recommendations.tail())
    if asset.options:
        print("Options Dates Available:", asset.options)

def crypto_summary(crypto_symbol):
    crypto_asset = yf.Ticker(crypto_symbol)
    print(f"\nCrypto Summary for {crypto_symbol}:\n")
    print(crypto_asset.history(period="1mo"))

def export_to_csv(df, filename):
    df.to_csv(filename)
    print(f"File exported: {filename}")


# Visual Representation of Market Data

def display_dashboard(history, symbols):
    fig, axs = plt.subplots(3, 2, figsize=(15, 18), constrained_layout=True)
    axs = axs.flatten()

    for ticker in symbols:
        history[ticker]['Close'].plot(ax=axs[0], label=f'{ticker} Price')
    axs[0].set_title('Price Movement')
    axs[0].legend()
    axs[0].grid(True)

    closing_df = pd.DataFrame({sym: history[sym]['Close'] for sym in symbols})
    sns.heatmap(closing_df.corr(), annot=True, cmap='coolwarm', ax=axs[1])
    axs[1].set_title('Price Correlation')

    volumes = pd.DataFrame({sym: history[sym]['Volume'] for sym in symbols})
    volumes.plot(ax=axs[2])
    axs[2].set_title('Trade Volume Trends')

    returns_df = closing_df.pct_change()
    returns_df.plot(ax=axs[3])
    axs[3].set_title('Percentage Returns')

    for i, sym in enumerate(symbols[:2]):
        sns.histplot(returns_df[sym].dropna(), kde=True, ax=axs[4 + i], color='orange')
        axs[4 + i].set_title(f'{sym} Return Distribution')

    plt.show()


# Data Science Workflow: SQL, Forecasting, Risk Analysis

def run_analysis():
    apple_data = pd.read_csv('AAPL_stock_data.csv')
    all_stocks = pd.read_csv('stocks_data.csv', skiprows=2)

    all_stocks.columns = [
        'Date', 'AAPL_C', 'GOOGL_C', 'TSLA_C',
        'AAPL_H', 'GOOGL_H', 'TSLA_H',
        'AAPL_L', 'GOOGL_L', 'TSLA_L',
        'AAPL_O', 'GOOGL_O', 'TSLA_O',
        'AAPL_V', 'GOOGL_V', 'TSLA_V'
    ]

    apple_data['Date'] = pd.to_datetime(apple_data['Date'], utc=True).dt.tz_localize(None)
    all_stocks['Date'] = pd.to_datetime(all_stocks['Date'])

    connection = sqlite3.connect(':memory:')
    apple_data.to_sql('apple_tbl', connection, index=False)
    all_stocks.to_sql('stocks_tbl', connection, index=False)

    sql = """
    SELECT a.Date, a.Open AS Apple_Open, a.High AS Apple_High, a.Low AS Apple_Low, a.Close AS Apple_Close, a.Volume AS Apple_Volume,
           s.AAPL_O, s.AAPL_H, s.AAPL_L, s.AAPL_C, s.AAPL_V,
           s.GOOGL_O, s.GOOGL_H, s.GOOGL_L, s.GOOGL_C, s.GOOGL_V,
           s.TSLA_O, s.TSLA_H, s.TSLA_L, s.TSLA_C, s.TSLA_V
    FROM apple_tbl a
    JOIN stocks_tbl s ON date(a.Date) = date(s.Date)
    """

    merged = pd.read_sql(sql, connection, parse_dates=['Date']).set_index('Date')

    merged['Apple_Ret'] = merged['AAPL_C'].pct_change()
    merged['Google_Ret'] = merged['GOOGL_C'].pct_change()
    merged['Tesla_Ret'] = merged['TSLA_C'].pct_change()

    volatility_data = merged[['Apple_Ret', 'Google_Ret', 'Tesla_Ret']].std()

    model = ARIMA(merged['AAPL_C'].dropna(), order=(5, 1, 0))
    result = model.fit()
    future = result.forecast(steps=15)

    risk = {}
    threshold = 0.95
    for col in ['Apple_Ret', 'Google_Ret', 'Tesla_Ret']:
        value_at_risk = np.percentile(merged[col].dropna(), (1 - threshold) * 100)
        conditional_var = merged[col][merged[col] <= value_at_risk].mean()
        risk[col] = {'VaR': value_at_risk, 'CVaR': conditional_var}

    corr_data = merged[['AAPL_C', 'GOOGL_C', 'TSLA_C', 'AAPL_V', 'GOOGL_V', 'TSLA_V']].corr()

    fig, axs = plt.subplots(3, 2, figsize=(15, 18))

    sns.heatmap(corr_data, annot=True, ax=axs[0, 0])
    axs[0, 0].set_title('Correlation Heatmap')

    future.plot(ax=axs[0, 1], title='AAPL Forecast (ARIMA)')
    axs[0, 1].set_xlabel('Time Steps')
    axs[0, 1].set_ylabel('Predicted Price')

    merged[['Apple_Ret', 'Google_Ret', 'Tesla_Ret']].plot(ax=axs[1, 0], title='Return Trends')

    volatility_data.plot.bar(ax=axs[1, 1], title='Market Volatility')

    (1 + merged[['Apple_Ret', 'Google_Ret', 'Tesla_Ret']]).cumprod().plot(ax=axs[2, 0], title='Growth of $1 Investment')

    merged['Close_Diff'] = merged['Apple_Close'] - merged['AAPL_C']
    merged['Close_Diff'].plot(ax=axs[2, 1], marker='o', linestyle='', title='AAPL Close Price Variance')
    axs[2, 1].axhline(0, color='gray', linestyle='--')

    plt.tight_layout()
    plt.show()
    connection.close()


# Driver Code

if __name__ == "__main__":
    stock_list = input("Enter stock tickers separated by commas (e.g. AAPL, GOOGL, TSLA): ").split(",")
    stock_list = [ticker.strip().upper() for ticker in stock_list]

    price_data = get_stock_prices(stock_list)
    export_to_csv(price_data, "stocks_data.csv")
    display_dashboard(price_data, stock_list)
