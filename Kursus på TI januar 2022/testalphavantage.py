# Alpha Vantage API key: 
# 1HPAI293TV2TFCLH

from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='1HPAI293TV2TFCLH')
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('GOOGL')
print(data)
