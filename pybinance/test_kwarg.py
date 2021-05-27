import binance


#　監視する通貨
brands_list = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'NEOUSDT']

binance_api = binance.Binance()
check_15m = True
check_1h = True
check_4h = True
first_time = False

data15m = binance_api.get_brands_candle_data(brands_list,'15m')

data1h = binance_api.get_brands_candle_data(brands_list,'1h')

data4h = binance_api.get_brands_candle_data(brands_list,'4h')
  



def func1(*val):
    for value in val:
        print(value['BTCUSDT'].iat[-1])
        value['BTCUSDT'].iat[-1] = 400
        print(value['BTCUSDT'].iat[-1])






func1(data15m,data1h,data4h)