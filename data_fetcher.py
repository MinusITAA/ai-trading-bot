import requests

API_KEY = "594e51de581d4df69d4fb5433f31c8b5"

def get_price(symbol):
    url = f"https://api.twelvedata.com/price?symbol={symbol}&apikey={API_KEY}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            print(f"Errore HTTP {response.status_code} per {symbol}")
            return None
        data = response.json()
        if "price" in data:
            return float(data["price"])
        else:
            print(f"Errore nella risposta per {symbol}: {data}")
            return None
    except Exception as e:
        print(f"Errore durante la richiesta per {symbol}: {e}")
        return None