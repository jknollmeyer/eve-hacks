import requests
import json

prices_response = requests.get('https://esi.evetech.net/latest/markets/prices')

prices_json = json.loads(prices_response.text)
first_market_price_info = prices_json[0]
first_item_id = first_market_price_info["type_id"]
item_price = first_market_price_info["average_price"]

item_info_response = requests.get('https://esi.evetech.net/latest/universe/types/' + str(first_item_id))
item_info = json.loads(item_info_response.text)
item_name = item_info["name"]
item_description = item_info["description"]

print("Item name: " + item_name)
print("Item description: " + item_description)
print("Latest price: " + str(item_price) + " ISK")


#### PART 2
'''
r = requests.get('https://esi.evetech.net/latest/markets/groups')
print(r.text)

r = requests.get('https://esi.evetech.net/latest/markets/groups/23')
print(r.text)


r = requests.get('https://esi.evetech.net/latest/universe/types/13267')
print(r.text)


{
    "adjusted_price":4657392.151762767,
    "average_price":4577298.32,
    "type_id":32061
}

{"description":"Ferrying passengers can give a nice profit","market_group_id":23,"name":"Passengers","parent_group_id":19,"types":[17767,3810,13267,17796,17765,4358,3719,3721,3723,18029,12110,12049,12243,26902,3806,17791]}

{"adjusted_price":15053473.18144104,"average_price":24211306.31,"type_id":13265},{"adjusted_price":863.1654846911779,"average_price":17421.99,"type_id":13267}
'''