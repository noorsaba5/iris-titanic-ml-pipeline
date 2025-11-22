import yfinance as yf
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from io import BytesIO
date_default_start = pd.to_datetime("today") - pd.DateOffset(years=5)
date_default_end = pd.to_datetime("today")

st.set_page_config(page_title="Stock Price Dashboard", layout="wide")

st.title("📈 Stock Price Tracker Dashboard")

# Sidebar inputs
symbol = st.sidebar.text_input("Enter Stock Symbol (Example: TCS.NS):", value="TCS.NS")
start_date = st.sidebar.date_input("Start Date", value=date_default_start)
end_date = st.sidebar.date_input("End Date", value=date_default_end)

# Fetch data if symbol entered
if symbol and start_date and end_date:
    ticker = yf.Ticker(symbol)
    df = ticker.history(start=start_date, end=end_date)

    if df.empty:
        st.warning("No data found. Please check the symbol or date range.")
    else:
        df.reset_index(inplace=True)

        st.subheader(f"Historical Data for {symbol}")
        st.dataframe(df.tail(10))

        # Price Chart
        st.subheader(f"Closing Price Chart for {symbol}")
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(df['Date'], df['Close'], label='Close Price')
        ax.set_xlabel("Date")
        ax.set_ylabel("Price (INR)")
        ax.set_title(f"Closing Price for {symbol}")
        ax.grid(True)
        st.pyplot(fig)

        # Export price chart as PNG
        buffer = BytesIO()
        fig.savefig(buffer, format='png')
        st.download_button(label="Download Price Chart as PNG", data=buffer.getvalue(), file_name=f"{symbol}_price_chart.png")

        # Daily Returns Chart
        df['Daily Return'] = df['Close'].pct_change()
        st.subheader(f"Daily Return Chart for {symbol}")
        fig2, ax2 = plt.subplots(figsize=(12, 6))
        ax2.plot(df['Date'], df['Daily Return'], color='orange')
        ax2.set_xlabel("Date")
        ax2.set_ylabel("Daily Return")
        ax2.set_title(f"Daily Returns for {symbol}")
        ax2.grid(True)
        st.pyplot(fig2)

        # Export daily return chart as PNG
        buffer2 = BytesIO()
        fig2.savefig(buffer2, format='png')
        st.download_button(label="Download Daily Return Chart as PNG", data=buffer2.getvalue(), file_name=f"{symbol}_daily_return_chart.png")

        # Top gainers and losers
        st.subheader("Top 5 Gain Days:")
        st.table(df.sort_values(by='Daily Return', ascending=False).head(5)[['Date', 'Close', 'Daily Return']])

        st.subheader("Top 5 Loss Days:")
        st.table(df.sort_values(by='Daily Return').head(5)[['Date', 'Close', 'Daily Return']])
else:
    st.info("Please enter a stock symbol and select a date range to get started.")

# Deployment Note:
# - Save this file as app.py
# - Deploy by pushing to GitHub, linking to https://streamlit.io/cloud, and clicking 'Deploy'.
# - Add necessary libraries in requirements.txt (streamlit, yfinance, pandas, matplotlib).
