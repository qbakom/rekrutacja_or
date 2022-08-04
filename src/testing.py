from requests.exceptions import HTTPError
import requests
import json
import time
from datetime import datetime


def dodatkowe():
    response = call_api()
    data = response.json()
    for i in range(100):
        
        x = data["rates"][i]["mid"]
        date = data["rates"][i]["effectiveDate"]
        
        if x < 4.5 or x > 4.7:
            print(date)

def validate_json(data):
    try:
        json.loads(data)
    except ValueError as e:
        return False
    return True

def call_api():
    try:
        response = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/eur/last/100/?format=json")
        response.raise_for_status()
        return response
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

def print_data():
    #1
    response = call_api()

    now = datetime.now()
    data = "timestamp: " + str(now) + ", "

    #2
    total_seconds = str(response.elapsed.total_seconds())
    data += "response time: " + total_seconds + ", "

    #3
    status_code = str(response.status_code)
    data += "status code: " + status_code + ", "

    #4
    headers = response.headers["Content-Type"]
    s = headers.find(";")
    headers = response.headers["Content-Type"][:s]
    data += "content-type: " + str(headers) + ", "

    #5
    data += "JSON is valid:" + str(validate_json(response.content))
    print(data)

for i in range(10):
    print(i+1, end=" ")
    print_data()
    time.sleep(5)

dodatkowe()