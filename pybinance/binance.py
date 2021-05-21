
import talib
import sys
import requests
import time
import pandas as pd
import json



# vRsi = talib.RSI(dataFrame['Close'],14)
class Binance:

    def chartTimeToInteger(self,chartTime) -> int:
        if chartTime == "1m":
            return 60
        elif chartTime == "5m":
            return 300
        elif chartTime == "15m":
            return 900
        elif chartTime == "1h":
            return 3600
        elif chartTime == "4h":
            return 14400
        elif chartTime == "1d":
            return 86400
        else:
            return 0


    def getCandleData(self,symbol,chartTime,num) -> pd.DataFrame:
        chartTimeNum = self.chartTimeToInteger(chartTime)
        if chartTimeNum == 0:
            print("時間足入力エラー[1m,5m,15m,1h,4h,1d]")
            sys.exit()
        # print(chartTimeNum)
        # print(chartTimeNum*num)
        stamps=int(time.time() - chartTimeNum*num)*1000
        url="https://api.binance.com/api/v3/klines?symbol="+symbol+"&interval="+chartTime+"&startTime="+str(stamps)
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


    def getCurrentPrices(self) -> pd.DataFrame:
        res = requests.get("https://api.binance.com/api/v3/ticker/price")
        # DataFrameの作成
        df = pd.read_json(json.dumps(res.json()))
        df = df[df['symbol'].str.contains('USDT')]
        # print(df.columns)
        df.reset_index(drop=True ,inplace = True)
        # print(df.dtypes)
        
        print(df.transpose())
        return df

    def getCurrentBrandPrices(self,brands_list) -> pd.DataFrame:
        # 結果保存
        result_df = pd.DataFrame(index=[], columns=brands_list)

        df = self.getCurrentPrices()
        
        # print(df.columns)
        df.reset_index(drop=True ,inplace = True)
        # print(df.dtypes)
        return df

    def getBrands(self) -> list:
        res = requests.get("https://api.binance.com/api/v3/ticker/price")
        # DataFrameの作成
        df = pd.read_json(json.dumps(res.json()))
        df = df[df['symbol'].str.contains('USDT')]
        # df.drop(columns='price', axis=1, inplace=True)
        # print(df.columns)
        df.reset_index(drop=True ,inplace = True)
        # print(df.dtypes)
        return df['symbol'].tolist()

    def findBrand(self,brand) -> bool:
        return brand in self.getBrands()

    def getBrandsCandleData(self,brands_list,chartTime) -> pd.DataFrame:
        # 空のDataFrameの作成
        df = pd.DataFrame(index=[], columns=brands_list)

        for brand in brands_list:
            brand_candles = self.getCandleData(brand,chartTime,480)
            time.sleep(1)
            # print(brand_candles['Close'])
            if len(brand_candles.index) != 0:
                df[brand] = brand_candles['Close']
        
        return df
        # df.drop(columns='price', axis=1, inplace=True)
        # print(df.columns)
        # df.reset_index(drop=True ,inplace = True)
        # print(df.dtypes)
        # return df['symbol'].tolist()
    
    def changeTimeAxis(self,data) -> pd.DataFrame:
        # 空のDataFrameの作成
        print(data)


if __name__ == '__main__':

    #　監視する通貨
    brands_list = \
    ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'BCCUSDT', 'NEOUSDT', 'LTCUSDT', 'QTUMUSDT', 'ADAUSDT', \
    'XRPUSDT', 'HOTUSDT', 'SHIBUSDT', 'TRUUSDT', 'XLMUSDT', 'LINKUSDT', 'TRXUSDT', 'ETCUSDT', \
    'BANDUSDT', 'DAIUSDT', 'FTMUSDT', 'XEMUSDT', 'ADAUSDT' , 'KSMUSDT']

    # 15分足DataFrame

    # print(brands_list)

    binance = Binance()
    # df = binance.getCandleData("dsads","4h",5)
    # print(len(df.index) == 0)
    # print(binance.findBrand('ADAUSDT'))
    # print(binance.getBrandsCandleData( ['IRISUSDT' , 'KSMUSDT']))
    # print(binance.getBrands())
    
    # 空のDataFrameの作成

    data = pd.DataFrame(index=[], columns=brands_list)
    # data2 = binance.getCurrentPrices()
    # print(data2)
    # data3 = binance.getBrandsCandleData(['IRISUSDT','KSMUSDT','BTCUSDT'],'4h')
    # print(type(data2.index.values))
    
    # print(data2.iloc[-1])
    # print(data3.iloc[-1]['BTCUSDT'])

    res = requests.get("https://api.binance.com/api/v3/ticker/price")
        
    print(json.loads(json.dumps(res.json())))
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

