import requests

from_currency = input("From Currency: ").upper()
to_currency = input("To Currency: ").upper()
amount = float(input("Amount: "))

response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

print(f"${amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}")
