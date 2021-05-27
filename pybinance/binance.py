
import datetime
import notify
import talib
import sys
import requests
import time
import pandas as pd
import json


class Binance:

    def chart_time_to_integer(self,chart_time) -> int:
        if chart_time == "1m":
            return 60
        elif chart_time == "5m":
            return 300
        elif chart_time == "15m":
            return 900
        elif chart_time == "1h":
            return 3600
        elif chart_time == "4h":
            return 14400
        elif chart_time == "1d":
            return 86400
        else:
            return 0


    def get_candle_data(self,symbol,chart_time,num) -> pd.DataFrame:
        chart_time_number = self.chart_time_to_integer(chart_time)
        if chart_time_number == 0:
            print("時間足入力エラー[1m,5m,15m,1h,4h,1d]")
            sys.exit()
        # print(chartTimeNum)
        # print(chartTimeNum*num)
        stamps=int(time.time() - chart_time_number*num)*1000
        url="https://api.binance.com/api/v3/klines?symbol="+symbol+"&interval="+chart_time+"&startTime="+str(stamps)
        res=requests.get(url)

        # DataFrameの作成
        df = pd.DataFrame(data=res.json(), columns=['OpenTime', 'Open', 'High' , 'Low' , 'Close' , 'Volume' , 'CloseTime' ,'A','B','C','D','E'])
        df.drop(columns=['Volume','CloseTime','A','B','C','D','E'], axis=1, inplace=True)

        # 時間のdatetime化
        df['OpenTime'] = (df['OpenTime']/1000).astype('int64')
        df['OpenTime'] = pd.to_datetime(df['OpenTime'],unit='s')

        # Objectをfloatに変換
        df['Open']  = df['Open'].astype(float, errors = 'raise')
        df['Close'] = df['Close'].astype(float, errors = 'raise')
        df['High']  = df['High'].astype(float, errors = 'raise')
        df['Low']   = df['Low'].astype(float, errors = 'raise')
        return df


    def get_current_prices(self) -> pd.DataFrame:
        res = requests.get("https://api.binance.com/api/v3/ticker/price")
        # DataFrameの作成
        df = pd.read_json(json.dumps(res.json()))
        df = df[df['symbol'].str.contains('USDT')]
        # print(df.columns)
        df.reset_index(drop=True ,inplace = True)
        # print(df.dtypes)
        
        print(df.transpose())
        return df

    def get_current_price_list(self) -> list:
        res = requests.get("https://api.binance.com/api/v3/ticker/price")
        return res.json()

    def get_current_brand_prices(self,brands_list) -> pd.DataFrame:
        # 結果保存
        result_df = pd.DataFrame(index=[], columns=brands_list)

        df = self.get_current_prices()
        
        # print(df.columns)
        df.reset_index(drop=True ,inplace = True)
        # print(df.dtypes)
        return df

    def get_brands(self) -> list:
        res = requests.get("https://api.binance.com/api/v3/ticker/price")
        # DataFrameの作成
        df = pd.read_json(json.dumps(res.json()))
        df = df[df['symbol'].str.contains('USDT')]
        # df.drop(columns='price', axis=1, inplace=True)
        # print(df.columns)
        df.reset_index(drop=True ,inplace = True)
        # print(df.dtypes)
        return df['symbol'].tolist()

    def find_brand(self,brand) -> bool:
        return brand in self.get_brands()

    def get_brands_candle_data(self,brands_list,chart_time) -> pd.DataFrame:
        # 空のDataFrameの作成
        df = pd.DataFrame(index=[], columns=brands_list)

        for brand in brands_list:
            brand_candles = self.get_candle_data(brand,chart_time,480)
            time.sleep(0.3)
            # print(brand_candles['Close'])
            if len(brand_candles.index) != 0:
                df[brand] = brand_candles['Close']
        
        return df

    def update(self,*dataframe) -> pd.DataFrame:
        cur = self.get_current_price_list()
        for df in dataframe:
            for brand in df.columns:
                print(brand)
                for item in cur:
                    if item['symbol'] == brand:
                        df[brand].iat[-1] = item['price']
                        break





    


if __name__ == '__main__':

    #　監視する通貨
    brands_list = \
    ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'BCCUSDT', 'NEOUSDT', 'LTCUSDT', 'QTUMUSDT', 'ADAUSDT', \
    'XRPUSDT', 'HOTUSDT', 'SHIBUSDT', 'TRUUSDT', 'XLMUSDT', 'LINKUSDT', 'TRXUSDT', 'ETCUSDT', \
    'BANDUSDT', 'DAIUSDT', 'FTMUSDT', 'XEMUSDT', 'ADAUSDT' , 'KSMUSDT']


    binance = Binance()
    # df = binance.getCandleData("dsads","4h",5)
    
    data3 = binance.get_brands_candle_data(['IRISUSDT','KSMUSDT','BTCUSDT'],'4h')
    # print(type(data2.index.values))
    # print(data3)
    print(data3)

    time.sleep(1)
    binance.update(data3)
    # print(data3['BTCUSDT'].iat[-1])
    print(data3)
    print(talib.RSI(data3['BTCUSDT'], timeperiod=14))

    notice = notify.Notify()
    notice.toDiscord("Hello")

    
    # print(data2.iloc[-1])
    # print(data3.iloc[-1]['BTCUSDT'])
    # print(data3)
        
    # df = pd.read_json(json.dumps(res.json()))

    '''
    for num in data2.index.values:
        # print(data2.iat[num,0])
        # print(type(num))
        for brand in data.columns:
            if data2.iat[num,0] == brand:
                print(data2.iat[num,0],data2.iat[num,1])
    '''

    # print(data)

    '''
    while True:
        df_1h = binance.getBrandsCandleData(brands_list,'1h')
        df_4h = 
    '''

