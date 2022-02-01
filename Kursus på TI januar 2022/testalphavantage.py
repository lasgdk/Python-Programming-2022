# Install library for alpha vantage support: 
#  pip install alpha_vantage pandas
# Alpha Vantage API key: 
#  1HPAI293TV2TFCLH

from alpha_vantage.techindicators import TechIndicators

api_key = 'RNZPXZ6Q9FEFMEHM'

LOW_RSI=30
HIGH_RSI=70

import requests
import pandas
import time

ti = TechIndicators(key=api_key, output_format='pandas')

symbollist = ['ALMB.OMCX', 'GOOG']

for symbol in symbollist:
    print("Working on symbol: "+symbol)

    data_weekly,meta = ti.get_rsi(symbol=symbol, interval='weekly')
    current_weekly_rsi=data_weekly.iloc[-1].tolist()
    data_daily,meta = ti.get_rsi(symbol=symbol, interval='daily')
    current_daily_rsi=data_daily.iloc[-1].tolist()
    print("Current RSI value based on weekly values for symbol "+symbol+" is: "+str(current_weekly_rsi[0]))
    print("Current RSI value based on daily values for symbol "+symbol+" is: "+str(current_daily_rsi[0]))
    if current_weekly_rsi[0] < LOW_RSI:
        print("Hey, the RSI value of "+symbol+" is currently quite low! It is "+str(current_weekly_rsi[0]))
    if current_weekly_rsi[0] > HIGH_RSI:
        print("Hey, the RSI value of "+symbol+" is currently quite high! It is "+str(current_weekly_rsi[0]))
    if current_daily_rsi[0] < LOW_RSI:
        print("Hey, the RSI value of "+symbol+" is currently quite low! It is "+str(current_daily_rsi[0]))
    if current_daily_rsi[0] > HIGH_RSI:
        print("Hey, the RSI value of "+symbol+" is currently quite high! It is "+str(current_daily_rsi[0]))
    print("Finished working on symbol: "+symbol)
    print("Waiting about a minute, as we can only do 5 calls per minute on free plan.",end="")
    time.sleep(21)
    print("...",end="")
    time.sleep(21)
    print("...",end="")
    time.sleep(21)
    print("...")



# def get_rsi(self, symbol, interval='daily', time_period=20, series_type='close'):
#         """ Return the relative strength index time series in two json
#         objects as data and meta_data. It raises ValueError when problems arise
#         Keyword Arguments:
#             symbol:  the symbol for the equity we want to get its data
#             interval:  time interval between two conscutive values,
#                 supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
#                 'weekly', 'monthly' (default 'daily')
#             time_period:  How many data points to average (default 20)
#             series_type:  The desired price type in the time series. Four types
#                 are supported: 'close', 'open', 'high', 'low' (default 'close')
#         """
#         _FUNCTION_KEY = "RSI"
#         return _FUNCTION_KEY, 'Technical Analysis: RSI', 'Meta Data'