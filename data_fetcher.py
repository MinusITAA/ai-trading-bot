import requests

API_KEY = "594e51de581d4df69d4fb5433f31c8b5"

def get_price(symbol):
    url = f"https://api.twelvedata.com/price?symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return float(data["price"]) if "price" in data else None