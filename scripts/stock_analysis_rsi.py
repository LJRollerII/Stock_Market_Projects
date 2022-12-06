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


combined = pd.DataFrame()
combined['Adj Close']  = data['Adj Close']
combined['RSI'] = RSI

plt.figure(figsize=(12,8))
axis1 = plt.subplot(211)
axis1.plot(combined.index, combined['Adj Close'], color='lightgray')
axis1.set_title("Adjusted Close Price", color='white')

axis1.grid(True, color='#555555')
axis1.set_axisbelow(True)
axis1.set_facecolor('black')
axis1.figure.set_facecolor('#121212')
axis1.tick_params(axis='x', colors='white')
axis1.tick_params(axis='y', colors='white')

axis2 = plt.subplot(212, sharex=axis1)
axis2.plot(combined.index, combined['RSI'], color='lightgray')
axis2.axhline(0, linestyle='--', alpha=0.5, color='#ff0000')
axis2.axhline(10, linestyle='--', alpha=0.5, color='#ffaa00')
axis2.axhline(20, linestyle='--', alpha=0.5, color='#00ff00')
axis2.axhline(30, linestyle='--', alpha=0.5, color='#cccccc')
axis2.axhline(70, linestyle='--', alpha=0.5, color='#cccccc')
axis2.axhline(80, linestyle='--', alpha=0.5, color='#00ff00')
axis2.axhline(90, linestyle='--', alpha=0.5, color='#ffaa00')
axis2.axhline(100, linestyle='--', alpha=0.5, color='#ff0000')

axis2.set_title("RSI Value")
axis2.grid(False)
axis2.set_axisbelow(True)
axis2.set_facecolor('black')
axis2.tick_params(axis='x', colors='white')
axis2.tick_params(axis='y', colors='white')

plt.show()