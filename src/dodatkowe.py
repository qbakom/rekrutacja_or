import requests

response = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/eur/last/100/?format=json") 
resp = response.json()

for i in range(100):
    for x in resp["rates"][i]["mid"]:
        print(x)