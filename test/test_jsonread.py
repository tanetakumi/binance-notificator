import requests
import json


res = requests.get("https://api.binance.com/api/v3/ticker/price")
data = res.json()

print(type(data))
for item in data:
    if item['symbol'] == 'BTCUSDT':
        print(item['price'])
# print(json.loads(json.dumps(res.json())))

