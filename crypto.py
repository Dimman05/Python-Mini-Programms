import pandas_datareader as web 
import matplotlib.pyplot as plt 
import mplfinance as mpf 
import datetime as dt 

crypto = input("Enter a cryptocoin(In Capitals):")
currency = "USD"

start = dt.datetime(2020, 7, 1)
end = dt.datetime.now()

data = web.DataReader(f"{crypto}-{currency}", "yahoo", start=start, end=end)

mpf.plot(data, type="candle", volume=True, style="yahoo")