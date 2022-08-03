from turtle import right
import requests

response = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/eur/last/100/?format=json") 
resp = response.json()

for i in range(100):
    x = resp["rates"][i]["mid"]
    date = resp["rates"][i]["effectiveDate"]
    if x < 4.5 or x > 4.7:
        print(date)