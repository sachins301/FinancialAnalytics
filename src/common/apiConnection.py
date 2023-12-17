import requests
import json

baseUrl = 'https://api.iex.cloud/v1/'
tickerDataUrl = 'data/core/quote/'
ticker = 'aapl'
token = 'pk_d19d7d23bf2148e6988e3f61377d6355'

def getQuote():
    url = baseUrl+tickerDataUrl+ticker
    print(url)
    api = requests.get(url,{'token': 'pk_d19d7d23bf2148e6988e3f61377d6355'}).text
    quote = json.loads(api)
    print(api)

getQuote()