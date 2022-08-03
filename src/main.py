import requests
import json
import time

def validate_JSON(data):
    try:
        json.loads(data)
    except ValueError as e:
        return False
    return True

file = open("log.txt","w")

for i in range(10):
    response = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/eur/last/100/?format=json")    #1
    print(response.elapsed.total_seconds())     #2
    # file.write(f"{response.elapsed.total_seconds()}\n")

    #3
    print(response)
    
    if response.headers.get("content-type") == "application/json":      #4
        print("it's a json JSON")
        file.write(f"it's a json JSON\n")
    else:
        print("it's not a JSON")

    response = response.json()
    print(validate_JSON(response))   #5
    time.sleep(5)