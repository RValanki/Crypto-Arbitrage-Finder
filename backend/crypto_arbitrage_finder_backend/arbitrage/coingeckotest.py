import requests

def get_coin_tickers(coin_id):
    url = f'https://api.coingecko.com/api/v3/coins/{coin_id}/tickers'

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        print(f"First 10 Tickers for {data['name']}:")
        for index, ticker in enumerate(data['tickers'][:10], start=1):
            print(
                f"{index}. Exchange: {ticker['market']['name']}, "
                f"Pair: {ticker['base']}/{ticker['target']}, "
                f"Price: ${ticker['last']:.2f}, "
                f"Volume: {ticker['volume']:,}"
            )
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)

# List of top 10 cryptocurrencies by coin_id
top_ten_cryptos = [
    'bitcoin', 'ethereum', 'tether', 'binancecoin', 'usd-coin',
    'ripple', 'cardano', 'solana', 'dogecoin', 'tron'
]

# Call the function for each cryptocurrency in the top ten
for coin_id in top_ten_cryptos:
    get_coin_tickers(coin_id)
    print("\n" + "-"*50 + "\n")  # Separator between different coins' tickers
