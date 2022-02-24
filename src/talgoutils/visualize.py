from matplotlib.pyplot import title
import requests
import json
import pandas as pd
import mplfinance as mpl

def plot_candlestick_graph(df):
    df.date = pd.to_datetime(df.date)
    df.set_index('date', inplace=True)
    df.columns = df.columns[:].str.capitalize()
    return mpl.plot(df, type="candle", title = "Kite", style="yahoo")
