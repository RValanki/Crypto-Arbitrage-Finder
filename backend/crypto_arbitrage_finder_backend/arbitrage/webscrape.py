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
                "last_traded": ticker_data.get("last_traded_at", "N/A"),
                "market": ticker_data["market"]  # Store market info for detailed exchange info
            }
            result.append(market_info)
        
        return result
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

def find_arbitrage_opportunities(market_data):
    # Dictionary to hold exchanges by trading pair
    pairs_dict = {}
    arbitrage_opportunities = []

    # Organize data by trading pair
    for data in market_data:
        pair = data["pair"]
        if pair not in pairs_dict:
            pairs_dict[pair] = []
        pairs_dict[pair].append(data)

    # Check for arbitrage opportunities
    for pair, exchanges in pairs_dict.items():
        # Compare each exchange with others for the same pair
        for i in range(len(exchanges)):
            for j in range(i + 1, len(exchanges)):
                buy_exchange = exchanges[i]
                sell_exchange = exchanges[j]
                
                # Ensure different exchanges
                if buy_exchange["exchange"] != sell_exchange["exchange"]:
                    # Determine buy and sell prices based on price comparison
                    if buy_exchange["price"] < sell_exchange["price"]:
                        buy_price = buy_exchange["price"]
                        sell_price = sell_exchange["price"]
                        buy_exchange_name = buy_exchange["exchange"]
                        sell_exchange_name = sell_exchange["exchange"]
                        buy_exchange_info = buy_exchange  # Full object for buy exchange
                        sell_exchange_info = sell_exchange  # Full object for sell exchange
                    else:
                        buy_price = sell_exchange["price"]
                        sell_price = buy_exchange["price"]
                        buy_exchange_name = sell_exchange["exchange"]
                        sell_exchange_name = buy_exchange["exchange"]
                        buy_exchange_info = sell_exchange  # Full object for buy exchange
                        sell_exchange_info = buy_exchange  # Full object for sell exchange

                    # Calculate profit in absolute terms and percentage
                    profit = sell_price - buy_price
                    profit_percentage = (profit / buy_price) * 100

                    # Append only if profit is positive
                    if profit > 0:
                        arbitrage_opportunity = {
                            "pair": pair,
                            "buy_exchange": buy_exchange_name,
                            "sell_exchange": sell_exchange_name,
                            "profit": profit,
                            "profit_percentage": profit_percentage,
                            "buy_exchange_info": buy_exchange_info,
                            "sell_exchange_info": sell_exchange_info
                        }
                        arbitrage_opportunities.append(arbitrage_opportunity)

    return arbitrage_opportunities

# Example usage
btc_market_data = fetch_market_data("bitcoin")
if btc_market_data:
    arbitrage_opportunities = find_arbitrage_opportunities(btc_market_data)
    for opportunity in arbitrage_opportunities:
        print(opportunity)
        print('n')
