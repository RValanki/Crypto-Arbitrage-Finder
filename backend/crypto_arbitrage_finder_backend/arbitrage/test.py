import asyncio
import requests
from adapters.binance_adapter import BinanceAdapter  # Importing the BinanceAdapter class
from adapters.coinbase_adapter import CoinbaseAdapter  # Importing the CoinbaseAdapter class

def fetch_top_cryptos():
    # Fetching top 1000 cryptocurrencies from CoinGecko
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 200,
        'page': 1,
        'sparkline': False,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return [coin['symbol'].upper() + '/USDT' for coin in response.json()]
    else:
        print(f"Error fetching top cryptocurrencies: {response.status_code}")
        return []

async def fetch_binance_data(adapter):
    try:
        raw_data = await adapter.fetch_data()  # Fetch raw data asynchronously
        return adapter.normalize_data(raw_data)
    except Exception as e:
        print(f"Error fetching data for {adapter.symbol}: {e}")
        return None  # Return None on error

async def test_binance_adapter_multiple_cryptos():
    top_symbols = fetch_top_cryptos()  # Get top 1000 cryptocurrencies

    tasks = [fetch_binance_data(BinanceAdapter(symbol)) for symbol in top_symbols]
    normalized_data_list = await asyncio.gather(*tasks)

    successful_fetches = sum(1 for data in normalized_data_list if data is not None)

    print(f"Number of successful fetches from Binance: {successful_fetches}")
    for normalized_data in normalized_data_list:
        if normalized_data:
            print("Binance Normalized Data:", normalized_data)

async def fetch_coinbase_data(adapter):
    try:
        raw_data = await adapter.fetch_data()
        return adapter.normalize_data(raw_data)
    except Exception as e:
        print(f"Error fetching data for {adapter.symbol}: {e}")
        return None  # Return None on error

async def test_coinbase_adapter_multiple_cryptos():
    top_symbols = fetch_top_cryptos()  # Get top 1000 cryptocurrencies

    tasks = [fetch_coinbase_data(CoinbaseAdapter(symbol.replace('/', '-'))) for symbol in top_symbols]
    normalized_data_list = await asyncio.gather(*tasks)

    successful_fetches = sum(1 for data in normalized_data_list if data is not None)

    print(f"Number of successful fetches from Coinbase: {successful_fetches}")
    for normalized_data in normalized_data_list:
        if normalized_data:
            print("Coinbase Normalized Data:", normalized_data)

if __name__ == "__main__":
    print("Testing Binance Adapter for top 1000 cryptocurrencies...")
    asyncio.run(test_binance_adapter_multiple_cryptos())
    print("\nTesting Coinbase Adapter for top 1000 cryptocurrencies...")
    asyncio.run(test_coinbase_adapter_multiple_cryptos())
