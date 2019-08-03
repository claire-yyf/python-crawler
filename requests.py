# get API

import json
import requests

r = requests.get("https://jsonplaceholder.typicode.com/posts")
result = json.loads(r.text)  # json to python dict

userDict = {}

for i in range(len(result)):
    id = str(result[i]["userId"])
    if id in userDict:
        userDict[id] += 1
    else:
        userDict[id] = 1

print(userDict)
