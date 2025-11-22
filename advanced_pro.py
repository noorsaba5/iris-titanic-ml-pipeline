import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import numpy as np
import sqlite3
from statsmodels.tsa.arima.model import ARIMA
from plotly.subplots import make_subplots

def interactive_dashboard_with_filters():
    # Load CSVs
    apple_df = pd.read_csv('AAPL_stock_data.csv')
    stock_df = pd.read_csv('stocks_data.csv', skiprows=2)

    # Rename and parse dates
    stock_df.columns = [
        'Date', 'AAPL_Close', 'GOOGL_Close', 'TSLA_Close',
        'AAPL_High', 'GOOGL_High', 'TSLA_High',
        'AAPL_Low', 'GOOGL_Low', 'TSLA_Low',
        'AAPL_Open', 'GOOGL_Open', 'TSLA_Open',
        'AAPL_Volume', 'GOOGL_Volume', 'TSLA_Volume'
    ]
    stock_df['Date'] = pd.to_datetime(stock_df['Date'])
    stock_df.set_index('Date', inplace=True)

    # Build interactive figure using one default stock
    default_stock = 'AAPL'

    def build_filtered_figure(stock_symbol):
        # Extract columns
        close_col = f"{stock_symbol}_Close"
        volume_col = f"{stock_symbol}_Volume"

        # Compute daily and cumulative returns
        df = stock_df[[close_col, volume_col]].dropna()
        df['Daily_Return'] = df[close_col].pct_change()
        df['Cumulative_Return'] = (1 + df['Daily_Return']).cumprod()

        # Create figure with subplots
        fig = make_subplots(
            rows=3, cols=1,
            shared_xaxes=True,
            vertical_spacing=0.1,
            subplot_titles=(
                f"{stock_symbol} Closing Price & Volume",
                "Daily Returns",
                "Cumulative Returns"
            )
        )

        # Price and Volume (row 1)
        fig.add_trace(go.Scatter(x=df.index, y=df[close_col], mode='lines', name='Close Price'), row=1, col=1)
        fig.add_trace(go.Bar(x=df.index, y=df[volume_col], name='Volume', marker_color='lightblue', opacity=0.5), row=1, col=1)

        # Daily Returns (row 2)
        fig.add_trace(go.Scatter(x=df.index, y=df['Daily_Return'], mode='lines', name='Daily Return'), row=2, col=1)

        # Cumulative Returns (row 3)
        fig.add_trace(go.Scatter(x=df.index, y=df['Cumulative_Return'], mode='lines+markers', name='Cumulative Return'), row=3, col=1)

        # Layout
        fig.update_layout(
            height=800,
            title=f"📊 Interactive Dashboard: {stock_symbol}",
            template="plotly_white",
            xaxis_rangeslider_visible=True,
            updatemenus=[
                dict(
                    buttons=[
                        dict(label='AAPL', method='update',
                             args=[{'y': [
                                 stock_df['AAPL_Close'],
                                 stock_df['AAPL_Volume'],
                                 stock_df['AAPL_Close'].pct_change(),
                                 (1 + stock_df['AAPL_Close'].pct_change()).cumprod()
                             ]},
                                 {'title': "📊 Interactive Dashboard: AAPL"}]),
                        dict(label='GOOGL', method='update',
                             args=[{'y': [
                                 stock_df['GOOGL_Close'],
                                 stock_df['GOOGL_Volume'],
                                 stock_df['GOOGL_Close'].pct_change(),
                                 (1 + stock_df['GOOGL_Close'].pct_change()).cumprod()
                             ]},
                                 {'title': "📊 Interactive Dashboard: GOOGL"}]),
                        dict(label='TSLA', method='update',
                             args=[{'y': [
                                 stock_df['TSLA_Close'],
                                 stock_df['TSLA_Volume'],
                                 stock_df['TSLA_Close'].pct_change(),
                                 (1 + stock_df['TSLA_Close'].pct_change()).cumprod()
                             ]},
                                 {'title': "📊 Interactive Dashboard: TSLA"}])
                    ],
                    direction='down',
                    showactive=True,
                    x=0.5,
                    xanchor="center",
                    y=1.1,
                    yanchor="top"
                )
            ]
        )

        fig.update_xaxes(title_text="Date", row=3, col=1)
        fig.update_yaxes(title_text="Price / Volume", row=1, col=1)
        fig.update_yaxes(title_text="Daily Return", row=2, col=1)
        fig.update_yaxes(title_text="Cumulative Return", row=3, col=1)

        return fig

    # Show the default dashboard
    fig = build_filtered_figure(default_stock)
    fig.show()

# Run the dashboard if the script is executed directly
if __name__ == "__main__":
    run_dashboard = input("Launch interactive dashboard with dropdowns and date slider? [y/n]: ").strip().lower()
    if run_dashboard == 'y':
        interactive_dashboard_with_filters()
    else:
        print("Dashboard not launched.")
