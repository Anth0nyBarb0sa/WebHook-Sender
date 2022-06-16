import requests
import json

url = "ENTER A URL"


data = {"Message": "Hello World!"}

r = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

print(r)