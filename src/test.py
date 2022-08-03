import requests
import json

response = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/eur/last/100/?format=json")
print(response)