import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from thetadata import ThetaClient, OptionReqType, OptionRight, DateRange

def create_signals(ticker, exp_date, client):
    transactions = {
        "transaction_date": [],
        "ticker": [],
        "strike_price": [],
        "exp_date": [],
        "transaction_type": []
    }

    strikes = client.get_strikes(ticker, exp_date)
    for strike in strikes:
        try:
            data = client.get_hist_option(
                req=OptionReqType.EOD,
                root=ticker,
                exp=exp_date,
                strike=strike,
                right=OptionRight.CALL,
                date_range=DateRange(exp_date - dt.timedelta(90), exp_date)
            )

            if len(data) > 10:
                data.columns = ["Open", "High", "Low", "Close", "Volume", "Count", "Date"]
                data.set_index("Date", inplace=True)
                data['Signal'] = data['Volume'] > data['Volume'].mean() + 3 * data['Volume'].std()
                selected_data = data[data['Signal']]

                for index in selected_data.iterrows():
                    transactions['transaction_date'].append(index)
                    transactions['ticker'].append(ticker)
                    transactions['strike'].append(strike)
                    transactions['exp_date'].append(exp_date)
                    transactions['transaction_type'].append("buy")
        except Exception as e:
            continue

        try:
            data = client.get_hist_option(
                req=OptionReqType.EOD,
                root=ticker,
                exp=exp_date,
                strike=strike,
                right=OptionRight.PUT,
                date_range=DateRange(exp_date - dt.timedelta(90), exp_date)
            )

            if len(data) > 10:
                data.columns = ["Open", "High", "Low", "Close", "Volume", "Count", "Date"]
                data.set_index("Date", inplace=True)
                data['Signal'] = data['Volume'] > data['Volume'].mean() + 3 * data['Volume'].std()
                selected_data = data[data['Signal']]

                for index in selected_data.iterrows():
                    transactions['transaction_date'].append(index)
                    transactions['ticker'].append(ticker)
                    transactions['strike'].append(strike)
                    transactions['exp_date'].append(exp_date)
                    transactions['transaction_type'].append("sell")
        except Exception as e:
            continue

pd.DataFrame(transactions).to_csv("transactions.csv")

client = ThetaClient()

with client.connect():
    ticker = "BMY"
    exp_dates = client.get_expirations(ticker)

    for exp_date in exp_dates[390:400]:
        try:
            create_signals(ticker, exp_date, client)
        except:
            continue
