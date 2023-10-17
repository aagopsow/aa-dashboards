# Date created: October 16, 2023

# This script imports token prices calling Binance's api using
# code taken from geeksforgeeks article

import json
import requests

# request url
key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

# data from url
data = requests.get(key)
data = data.json()
print(f"{data['symbol']} price is {data['price']}")
