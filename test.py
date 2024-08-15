import json
import requests
import typing

def get_to_do_item(list_item: typing.Optional[int] = 1):
    api_url = f"https://jsonplaceholder.typicode.com/todos/{list_item}"
    response = requests.get(api_url)
    json_res = response.json()
    #print(json_res)
    return json_res

get_item = get_to_do_item(1)
print(get_item)