import requests
import time
import bs4
from bs4 import BeautifulSoup

keyword = 'ryzen'
results = []

for i in range(1,11):
    r = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_nkw='+keyword+'&_pgn='+str(i))
    print('r.status_code=',r.status_code)
    soup = BeautifulSoup(r.text, 'html.parser')
    boxes = soup.select('li.s-item--watch-at-corner.s-item')
    for box in boxes:
        print('---')
        result = {}
        items = box.select('.s-item__title')
        for item in items:
            #print('items=',item.text)
            result['item'] = item.text

        prices = box.select('.s-item__price')
        for price in prices:
            #print('prices=',price.text)
            result['price'] = price.text
            
        conditions = box.select('.SECONDARY_INFO')
        for condition in conditions:
            result['condition'] = condition.text

        print('result=',result)
        results.append(result)

import json
j = json.dumps(results)
with open('items.json','w') as f:
    f.write(j)