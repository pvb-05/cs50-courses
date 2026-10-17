# submit50 cs50/problems/2022/python/bitcoin
import sys
import requests
import json

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
elif len(sys.argv) == 2:
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

try:
    response = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=a6992073a0e46e268bbd592187650cfa18dc2ca352a17ed216492b43662c3a05')
    response = response.json()
    sum = n * float(response.get("data")["priceUsd"])
    print(f"${sum:,.4f}")
except requests.RequestException:
    sys.exit("Error")



