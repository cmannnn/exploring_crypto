# Exploring the Bitcoin market

import time, requests, json
import datetime as dt

# API access key
CMC_PRO_API_KEY = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'

# URL query and formatting
url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': CMC_PRO_API_KEY,
}

# fetch query
r = requests.get(url, headers=headers)

# checking for errors when fetching
if r.status_code == 200:
  response = json.loads(r.text)

# dump json file
with open('BTC_data.json','w') as f:
  json.dump(response, f)  




















