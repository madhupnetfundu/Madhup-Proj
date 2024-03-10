# https://jsonplaceholder.typicode.com/ --> great source for fake JSON

import requests
import json
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
print (todos == response.json())
print(type(todos))
print(todos[:2])