from numpy import NaN, nan
import binance
import math


binance_api = binance.Binance()

#　監視する通貨
brands_list = ['BNBUSDT','SHIBUSDT', 'TRUUSDT', 'XLMUSDT']


data4h = binance_api.get_brands_candle_data(brands_list,'4h')


print(data4h)


print(not math.isnan(data4h['SHIBUSDT'].iat[-1]))