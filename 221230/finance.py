import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

days = 20
tickers = {
    'apple': 'AAPL',
    'facebook': 'FB',
    'google': 'GOOGL',
    'microsoft': 'MSFT',
    'netflix': 'NFLX',
    'amazon': 'AMZN'
}

def get_data(days, tickers):
    df = pd.DataFrame()
    for company in tickers.keys():
    #company = 'aaple'
        tkr = yf.Ticker(tickers[company])
        hist = tkr.history(period=f'{days}d')
        hist.index = hist.index.strftime('%d %B %Y')
        hist = hist[['Close']]
        hist.columns = ['company']
        hist = hist.T
        hist.index.name = 'Name'
        df = pd.concat([df, hist])
    return df

import altair as alt

companies = ['apple', 'facebook']
data = df.loc[companies]
data.sort_index()
data = data.T.reset_index()

data = pd.melt(data, id_vars=['Date']).rename(
    columns={'value': 'Stock Price(USD)'}
)