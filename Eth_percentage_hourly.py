from bs4 import BeautifulSoup
import pandas
import requests
import json

link = 'https://www.livecoinwatch.com/'

r = requests.get(link)
soup = BeautifulSoup(r.content, 'html.parser')
#soup.find_all('table')
df = pandas.read_html(str(soup),header = 0)
data = json.loads(df[0].to_json(orient = "records"))[1]
print(data['1h'])