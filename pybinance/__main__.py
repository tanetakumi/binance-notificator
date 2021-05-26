# from pybinance import *

# from pybinance import Bot
import binance
import datetime
import time




if __name__ == "__main__":

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
        time.sleep(1)
        
        if first_time:
            check_15m = True
            check_1h = True
            check_4h = True
            first_time = False
            
            data15m = binance_api.

            print("----Initalize----",now)
        
        # 15分に一回関数
        if m % 15 == 0:
            if not check_15m:
                # something to do
                
                print("15")
                check_15m = True
        else:
            check_15m = False
        
        # 1時間に一回関数
        if m == 0:
            if not check_1h:
                # something to do
                print("1h")
                check_1h = True
        else:
            check_1h = False

        # 4時間に一回関数
        if h % 4 == 0:
            if not check_4h:
                # something to do
                print("4h")
                check_4h = True
        else:
            check_4h = False