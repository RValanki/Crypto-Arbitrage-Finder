import requests
import time

# Base URLs for CoinGecko API
top_coins_url = "https://api.coingecko.com/api/v3/coins/markets"
tickers_url_template = "https://api.coingecko.com/api/v3/coins/{id}/tickers"

# Parameters to get top 10 coins by market cap in USD
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
}

# Function to make API calls with exponential backoff
def make_request(url, retries=5, backoff_factor=2, params=None):
    for attempt in range(retries):
        response = requests.get(url, params=params)
        
        # If the request is successful, return the response
        if response.status_code == 200:
            return response.json()
        
        # If rate-limited, wait before retrying
        elif response.status_code == 429:
            wait_time = backoff_factor ** attempt  # Exponential backoff
            print(f"Rate limit exceeded. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
        else:
            print(f"Request failed with status code {response.status_code}. Retrying...")
            time.sleep(1)  # Small delay before retrying
    
    # If all retries fail, raise an exception
    raise Exception(f"Failed to get data after {retries} retries.")

# Step 1: Fetch the top 10 coins
try:
    response = make_request(top_coins_url, params=params)
    top_coins = response

    # Step 2: Fetch tickers for each top coin with a delay
    for coin in top_coins:
        coin_id = coin["id"]
        tickers_url = tickers_url_template.format(id=coin_id)
        
        try:
            tickers_data = make_request(tickers_url, params=None)  # No need to pass params here
            print(f"\nTickers for {coin['name']} (ID: {coin_id}):")
            for ticker in tickers_data['tickers']:
                print(f"Market: {ticker['market']['name']}, Pair: {ticker['base']}/{ticker['target']}, Price: {ticker['last']} {ticker['target']}")
        
        except Exception as e:
            print(f"An error occurred for coin {coin_id}: {e}")
        
        # Delay to avoid exceeding rate limit
        time.sleep(3)  # 3-second delay per request

except Exception as e:
    print(f"An error occurred: {e}")
