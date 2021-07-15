import json
from types import SimpleNamespace
from json import JSONEncoder

# 1. Convert the following JSON to Python object.
# {
#     "home": {
#         "player":{
#             "username": "tester",
#             "age": 21,
#             "winningNumbers": [21,47,55]
#         }
#     }
# }

data = """{
    "home": {
        "player":{
            "username": "tester",
            "age": 21,
            "winningNumbers": [21,47,55]
        }
    }
}"""
x = json.loads(data)
print(x['home']['player']['username'])
