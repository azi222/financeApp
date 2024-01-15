import datetime

import pandas_datareader.data as web
import matplotlib.pyplot as plt
import yfinance as yf


def plot_rub_usd():
    yf.pdr_override()
    df = web.DataReader('USDRUB=X', datetime.datetime.today() - datetime.timedelta(days=365))

    fig, ax = plt.subplots()
    ax.plot(df.index, df['Close'])
    fig.autofmt_xdate()
    plt.show()


def plot_usd_btc():
    yf.pdr_override()
    df = web.DataReader('BTC-USD',  datetime.datetime.today() - datetime.timedelta(days=365))

    fig, ax = plt.subplots()
    ax.plot(df.index, df['Close'])
    fig.autofmt_xdate()
    plt.show()

