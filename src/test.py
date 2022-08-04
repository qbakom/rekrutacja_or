import requests
import json

def validate_JSON(data):
    try:
        json.loads(data)
    except ValueError as err:
        return False
    return True

response = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/eur/last/100/?format=json")


# print(response.json())
# file = open("json_data.txt","w")
# file.write(response.json())
# print(json.loads(response.json()))
# print(validate_JSON(response))

#testing content_type headers
data = "content-type: " + str(response.headers["Content-Type"])
print(data)
headers = response.headers["Content-Type"]
s = headers.find(";")
print(response.headers["Content-Type"][:s])