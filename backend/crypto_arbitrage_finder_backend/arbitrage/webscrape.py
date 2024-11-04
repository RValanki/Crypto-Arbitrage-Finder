import requests

def fetch_btc_markets():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/tickers"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for ticker in data.get("tickers", []):
            exchange = ticker["market"]["name"]
            pair = f"{ticker['base']}/{ticker['target']}"
            price = ticker["last"]
            volume = ticker["volume"]
            print(f"Exchange: {exchange}, Pair: {pair}, Price: {price}, Volume: {volume}")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

fetch_btc_markets()
