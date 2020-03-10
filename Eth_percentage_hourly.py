from bs4 import BeautifulSoup
import pandas
import requests
import json
import time

link = 'https://www.livecoinwatch.com/'

class Eth_price():
    def __init__(self, link):
        self.shit = link
    
    def Etherium(self):
        r = requests.get(self.shit)
        soup = BeautifulSoup(r.content, 'html.parser')
        #Quick tip, if you want to see all entries in livecoin just do print(df) and you'll see where the info gets pulled. 
        df = pandas.read_html(str(soup),header = 0)
        data = json.loads(df[0].to_json(orient = "records"))[1]
        # while True:
        #     print("The current price rate of " + data['Coin'] +  " per hour " + data['1h'])
        #     print("The current rate of " + data['Coin'] + " in the last 24 hours " + data['24h'])
        #     time.sleep(10)
        #     print("Current price of " + data['Liquidity ±2%'])
        return(data['Coin'], data['1h'], data['24h'], data['Liquidity ±2%'], data['Price'])


