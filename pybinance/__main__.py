# from pybinance import *

# from pybinance import Bot
import binance
import datetime
import time

def mylog(text : str) -> None:
    print("[Binance]"+datetime.datetime.now().strftime("%H:%M:%S")+" "+text)


if __name__ == "__main__":

    #　監視する通貨
    brands_list = \
    ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'NEOUSDT', 'LTCUSDT', 'QTUMUSDT', 'ADAUSDT', \
    'XRPUSDT', 'HOTUSDT', 'SHIBUSDT', 'TRUUSDT', 'XLMUSDT', 'LINKUSDT', 'TRXUSDT', 'ETCUSDT', \
    'BANDUSDT', 'FTMUSDT', 'XEMUSDT', 'KSMUSDT']
    # test用　上書きリスト
    # brands_list = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT']

    binance_api = binance.Binance()

    first_time = True
    check_15m = False
    check_1h = False
    check_4h = False

    data15m = None
    data1h = None
    data4h = None
    
    # 例えば20通貨なら0.5秒間隔で10秒×3の30秒
    # 0.3秒間隔であれば18秒　←

    while True:
        
        now = datetime.datetime.now()
        h = now.hour
        m = now.minute
        mylog("loop")
        
        if first_time:
            check_15m = True
            check_1h = True
            check_4h = True
            first_time = False
            
            data15m = binance_api.get_brands_candle_data(brands_list,'15m')
            print(data15m)
            mylog("15min complete")
            data1h = binance_api.get_brands_candle_data(brands_list,'1h')
            print(data1h)
            mylog("1h complete")
            data4h = binance_api.get_brands_candle_data(brands_list,'4h')
            print(data4h)
            mylog("4h complete")

            mylog("----Initalize----")

        # + ------------------------------------------------------------ +
        # | 毎回の関数                                                    |
        # + ------------------------------------------------------------ +
        binance_api.update(data15m,data1h,data4h)
        # print(data4h)
        
        # + ------------------------------------------------------------ +
        # | 回の関数　　                                                  |
        # + ------------------------------------------------------------ +
        if m % 15 == 0:
            if not check_15m:
                # something to do
                data15m = binance_api.get_brands_candle_data(brands_list,'15m')
                mylog("15m update complete")
                check_15m = True
        else:
            check_15m = False
        
        # 1時間に一回関数---------------
        if m == 0:
            if not check_1h:
                # something to do
                data1h = binance_api.get_brands_candle_data(brands_list,'1h')
                print("1h")
                check_1h = True
        else:
            check_1h = False

        # 4時間に一回関数---------------
        if h % 4 == 0:
            if not check_4h:
                # something to do
                data4h = binance_api.get_brands_candle_data(brands_list,'4h')
                print("4h")
                check_4h = True
        else:
            check_4h = False
        
        # loop　の休憩
        time.sleep(5)