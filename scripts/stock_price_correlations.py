import pandas_datareader as web
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

start = dt.datetime(2018, 1, 1)
end = dt.datetime.now()

tickers = ["FB","GOOG", "GS", "PFE" ,"KO", "NVDA", "NKE", "MRK", "ADDDF" "MSFT","TSLA","AAPL", "JPM", "CCL", "BA", "PEP"]
colnames = []

for ticker in tickers:
    data = web.DataReader(ticker, "yahoo", start, end)
    if len(colnames) == 0:
        combined = data[['Adj Close']].copy()
    else:
        combined = combined.join(data['Adj Close'])
    colnames.append(ticker)
    combined.columns = colnames

print(combined)

#plt.yscale("log")

#for ticker in tickers:
    #plt.plot(combined[ticker], label=ticker)

#plt.legend(loc="upper right")
#plt.show()

corr_data = combined.pct_change().corr(method="pearson")
sns.heatmap(corr_data, annot=True, cmap="coolwarm")

plt.show()