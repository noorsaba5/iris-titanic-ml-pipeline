import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def load_and_prepare_data():
    # Read datasets
    apple_data = pd.read_csv('AAPL_stock_data.csv')
    combined_data = pd.read_csv('stocks_data.csv', skiprows=2)

    # Rename columns for clarity
    combined_data.columns = [
        'Date', 'AAPL_Close', 'GOOGL_Close', 'TSLA_Close',
        'AAPL_High', 'GOOGL_High', 'TSLA_High',
        'AAPL_Low', 'GOOGL_Low', 'TSLA_Low',
        'AAPL_Open', 'GOOGL_Open', 'TSLA_Open',
        'AAPL_Volume', 'GOOGL_Volume', 'TSLA_Volume'
    ]
    
    # Convert date column and set as index
    combined_data['Date'] = pd.to_datetime(combined_data['Date'])
    combined_data.set_index('Date', inplace=True)

    return combined_data

def generate_dashboard(stock_data, ticker='AAPL'):
    # Prepare required columns
    close = stock_data[f'{ticker}_Close']
    volume = stock_data[f'{ticker}_Volume']
    
    # Compute returns
    daily_ret = close.pct_change()
    cumulative_ret = (1 + daily_ret).cumprod()

    # Create layout with subplots
    fig = make_subplots(
        rows=3, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.1,
        subplot_titles=(
            f'{ticker} Price and Volume',
            'Daily Return',
            'Cumulative Return'
        )
    )

    # Row 1: Price and Volume
    fig.add_trace(go.Scatter(x=close.index, y=close, name='Close'), row=1, col=1)
    fig.add_trace(go.Bar(x=volume.index, y=volume, name='Volume', marker_color='lightgrey', opacity=0.4), row=1, col=1)

    # Row 2: Daily Return
    fig.add_trace(go.Scatter(x=daily_ret.index, y=daily_ret, name='Daily % Change'), row=2, col=1)

    # Row 3: Cumulative Return
    fig.add_trace(go.Scatter(x=cumulative_ret.index, y=cumulative_ret, name='Cumulative Return', mode='lines+markers'), row=3, col=1)

    # Add dropdown menu
    fig.update_layout(
        title=f'Stock Dashboard: {ticker}',
        height=850,
        template='plotly_white',
        xaxis_rangeslider_visible=True,
        updatemenus=[dict(
            active=0,
            buttons=[
                dict(label='AAPL', method='update',
                     args=[{'y': [
                         stock_data['AAPL_Close'],
                         stock_data['AAPL_Volume'],
                         stock_data['AAPL_Close'].pct_change(),
                         (1 + stock_data['AAPL_Close'].pct_change()).cumprod()
                     ]},
                           {'title': 'Stock Dashboard: AAPL'}]),
                dict(label='GOOGL', method='update',
                     args=[{'y': [
                         stock_data['GOOGL_Close'],
                         stock_data['GOOGL_Volume'],
                         stock_data['GOOGL_Close'].pct_change(),
                         (1 + stock_data['GOOGL_Close'].pct_change()).cumprod()
                     ]},
                           {'title': 'Stock Dashboard: GOOGL'}]),
                dict(label='TSLA', method='update',
                     args=[{'y': [
                         stock_data['TSLA_Close'],
                         stock_data['TSLA_Volume'],
                         stock_data['TSLA_Close'].pct_change(),
                         (1 + stock_data['TSLA_Close'].pct_change()).cumprod()
                     ]},
                           {'title': 'Stock Dashboard: TSLA'}])
            ],
            direction='down',
            x=0.5,
            xanchor='center',
            y=1.1,
            yanchor='top'
        )]
    )

    # Update axis labels
    fig.update_xaxes(title_text='Date', row=3, col=1)
    fig.update_yaxes(title_text='Price / Volume', row=1, col=1)
    fig.update_yaxes(title_text='Daily Return', row=2, col=1)
    fig.update_yaxes(title_text='Cumulative Return', row=3, col=1)

    fig.show()

def main():
    user_input = input("Do you want to view the interactive stock dashboard? (y/n): ").strip().lower()
    if user_input == 'y':
        df = load_and_prepare_data()
        generate_dashboard(df, ticker='AAPL')
    else:
        print("Dashboard was not launched.")

if __name__ == '__main__':
    main()
