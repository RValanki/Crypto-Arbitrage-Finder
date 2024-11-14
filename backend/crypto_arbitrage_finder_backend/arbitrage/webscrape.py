import requests

# Function to get coin data from CoinGecko API
def get_coin_data(coin_name):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_name.lower()}"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error fetching the data for {coin_name}, Status Code: {response.status_code}")
        return {"image_url": "Not available", "market_cap": "Not available"}
    
    coin_data = response.json()
    
    # Extract the coin image
    image_url = coin_data['image']['large'] if 'image' in coin_data else "Image not found"
    
    # Extract the market cap
    market_cap = coin_data['market_data']['market_cap']['usd'] if 'market_data' in coin_data else "Market cap not found"
    
    return {
        "image_url": image_url,
        "market_cap": market_cap
    }

# Hardcoded top 20 cryptocurrencies
top_20_coins = [
    "bitcoin", "ethereum", "tether", "binancecoin", "usd-coin", "ripple", "dogecoin", "litecoin", "chainlink",
    "uniswap", "binance-usd", "polkadot", "stellar", "vechain", "wrapped-bitcoin", "cardano", "monero", "ethereum-classic", 
    "solana", "tron"
]

# Loop through the top 20 coins and fetch their data
for coin in top_20_coins:
    coin_data = get_coin_data(coin)
    
    if coin_data:
        print(f"{coin.capitalize()}:")
        print(f"  Image URL: {coin_data['image_url']}")
        print(f"  Market Cap: ${coin_data['market_cap']}")
        print("=" * 50)
    else:
        print(f"Failed to retrieve data for {coin.capitalize()}.")
        print("=" * 50)
