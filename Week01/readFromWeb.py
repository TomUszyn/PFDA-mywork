# Program to read from the web.
# Author: Tomasz Uszynski

import requests

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

response = requests.get(url)
data = response.json()
#print (data)
print (data['bpi']['EUR']['rate'])
