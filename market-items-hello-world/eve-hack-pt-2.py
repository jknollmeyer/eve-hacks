import requests
import json

page = 1

pyerite_matches = []

while True:
    prices_response = requests.get('https://esi.evetech.net/latest/markets/10000043/orders?page=' + str(page) + '&type_id=' + str(35))
    orders_json = json.loads(prices_response.text)

    for order in orders_json:
        pyerite_matches.append(order)

    if len(orders_json) < 1000:
        break

    page += 1
    print("Going to page " + str(page))
        
print(pyerite_matches)


