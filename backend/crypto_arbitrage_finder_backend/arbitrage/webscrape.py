import requests

def fetch_market_data(ticker):
    url = f"https://api.coingecko.com/api/v3/coins/{ticker}/tickers"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        result = []
        
        for ticker_data in data.get("tickers", []):
            market_info = {
                "exchange": ticker_data["market"]["name"],
                "pair": f"{ticker_data['base']}/{ticker_data['target']}",
                "price": ticker_data["last"],
                "volume": ticker_data["volume"],
                "trust_score": ticker_data.get("trust_score", "N/A"),
                "bid_ask_spread_percentage": ticker_data.get("bid_ask_spread_percentage", "N/A"),
                "last_traded": ticker_data.get("last_traded_at", "N/A")
            }
            print(market_info)
            print('\n')
            result.append(market_info)
        
        return result
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

# Example usage
btc_market_data = fetch_market_data("bitcoin")
