import requests
import json

def validate_JSON(data):
    try:
        json.loads(data)
    except ValueError as err:
        return False
    return True

response = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/eur/last/100/?format=json")


print(response.json())
# file = open("json_data.txt","w")
# file.write(response.json())
# print(json.loads(response.json()))
# print(validate_JSON(response))