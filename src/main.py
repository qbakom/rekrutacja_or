from multiprocessing.sharedctypes import Value
import requests
import json

def validate_JSON(data):
    try:
        json.load(data)
    except ValueError as err:
        return False
    return True

response = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/eur/last/100/?format=json")    #1
print(response.elapsed.total_seconds())     #2

#3

if response.headers.get("content-type") == "application/json":      #4
    print("it's a json JSON")
else:
    print("it's not a JSON")
    
print(validate_JSON(response.json()))   #5
