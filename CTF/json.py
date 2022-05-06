import urllib.request
import json


data = {
    "year": "2022a",
    "items": [true, ["skiing"], 1],
    "key": true
}
values = urllib.parse.urlencode(data).encode(encoding='UTF8')//注释1
headers = {'Content-Type': 'application/json'}
print(data)
print(values)
print(json.dumps(data))
print(json.dumps(data).encode())
request = urllib.request.Request(url='url', headers=headers, data=json.dumps(data).encode())
response = urllib.request.urlopen(request)