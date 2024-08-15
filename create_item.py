import requests
import typing

def create_to_do_item(id: typing.Optional[int] = 1, title: typing.Optional[str] = "default note", completed: typing.Optional[bool] = False):
    api_url = "https://jsonplaceholder.typicode.com/todos"
    todo = {"userId": id, "title": title, "completed": completed}
    response = requests.post(api_url, json=todo)
    result = response.json()
    code = response.status_code
    # print(result)
    # print(code)
    
    return response


# result = create_to_do_item(2, "Buy Eggs", False)
# print(result.json())

