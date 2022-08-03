import requests
import json
import time

def validate_JSON(data):
    try:
        json.loads(data)
    except ValueError as e:
        return False
    return True

response = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/eur/last/100/?format=json")    #1
print(response.elapsed.total_seconds())     #2
# file.write(f"{response.elapsed.total_seconds()}\n")
#3
print(response.status_code)

if response.headers.get("content-type") == "application/json":      #4
    print("it's a json JSON")
else:
    print("it's not a JSON")
response = response.json()
print(validate_JSON(response))   #5