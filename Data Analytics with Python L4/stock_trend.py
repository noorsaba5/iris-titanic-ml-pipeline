import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def fetch_stock_data(tickers, period="6mo"):
    data = yf.download(tickers, period=period)
    return data

def plot_stock_trends(data, tickers):
    plt.figure(figsize=(12,6))
    
    for ticker in tickers:
        plt.plot(data.index, data["Close"][ticker], label=f'{ticker} Closing Price')

    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.title(f'Stock Price Trends: {", ".join(tickers)}')
    plt.legend()
    plt.grid()
    plt.show()

def save_to_csv(data, filename):
    data.to_csv(filename)
    print(f"Data saved to {filename}")

def fetch_additional_info(ticker):
    stock = yf.Ticker(ticker)
    print(f"\nFetching additional data for {ticker}...")
    print("Market Cap:", stock.info.get("marketCap", "N/A"))
    print("P/E Ratio:", stock.info.get("trailingPE", "N/A"))
    print("Dividend Yield:", stock.info.get("dividendYield", "N/A"))
    print("Recent Dividends:\n", stock.dividends.tail())
    print("Stock Splits:\n", stock.splits.tail())
    print("Financials:\n", stock.financials.head())
    print("Balance Sheet:\n", stock.balance_sheet.head())
    print("Cash Flow Statement:\n", stock.cashflow.head())
    print("Analyst Recommendations:\n", stock.recommendations.tail())
    if stock.options:
        print("Available Option Expiration Dates:", stock.options)

def fetch_crypto_data(crypto_ticker):
    crypto = yf.Ticker(crypto_ticker)
    print(f"\nFetching cryptocurrency data for {crypto_ticker}...")
    print(crypto.history(period="1mo"))

if __name__ == "__main__":
    tickers = input("Enter stock ticker symbols separated by commas (e.g., AAPL, TSLA, GOOGL): ").split(",")
    tickers = [t.strip().upper() for t in tickers]  # Clean up input
    
    hist = fetch_stock_data(tickers)
    plot_stock_trends(hist, tickers)
    save_to_csv(hist, "stocks_data.csv")
    
    for ticker in tickers:
        fetch_additional_info(ticker)
    
    crypto_ticker = input("Enter cryptocurrency ticker (e.g., BTC-USD) or press Enter to skip: ")
    if crypto_ticker:
        fetch_crypto_data(crypto_ticker)
