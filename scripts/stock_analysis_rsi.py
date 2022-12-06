import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
import datetime as dt

ticker = 'PFE'
start = dt.datetime(2018, 1, 1)
end = dt.datetime.now()

data = web.DataReader(ticker, "yahoo", start, end)

delta = data['Adj Close'].diff(1)
delta.dropna(inplace=True)

positive = delta.copy()
negative = delta.copy()

positive[positive < 0] = 0
negative[negative > 0] = 0

days = 14

avg_gain = positive.rolling(window=days).mean()
avg_loss = abs(negative.rolling(window=days).mean())

relative_strength = avg_gain / avg_loss
RSI = 100.0 - (100.0 / (1.0 + relative_strength))

