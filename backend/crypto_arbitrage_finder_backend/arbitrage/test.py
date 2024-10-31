import asyncio
import requests
from adapters.binance_adapter import BinanceAdapter  # Adjust the import according to your project structure
from adapters.coinbase_adapter import CoinbaseAdapter
from adapters.kraken_adapter import KrakenAdapter
from adapters.bitfinex_adapter import BitfinexAdapter
from adapters.kucoin_adapter import KuCoinAdapter
from adapters.bybit_adapter import BybitAdapter  # Import the Bybit adapter
from adapters.huobi_adapter import HuobiAdapter  # Import the Huobi adapter

def fetch_top_cryptos():
    """Fetch the top cryptocurrencies from CoinGecko."""
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
        print(f"Error fetching top cryptocurrencies: {response.status_code}, Message: {response.text}")
        return []

async def fetch_and_normalize_data(adapter):
    """Fetch and normalize data from a given adapter."""
    try:
        raw_data = await adapter.fetch_data()  # Fetch raw data asynchronously
        if raw_data:
            return adapter.normalize_data(raw_data)
        else:
            print(f"No data returned for {adapter.symbol}.")
            return None
    except Exception as e:
        print(f"Error fetching data for {adapter.symbol}: {e}")
        return None  # Return None on error

async def test_adapter(adapter_class, top_symbols, symbol_normalization_func, fetch_all=False):
    """Test a specific adapter with multiple cryptocurrencies."""
    print(f"Testing {'fetch_all_data' if fetch_all else 'individual fetch'} method for {adapter_class.__name__}...")

    adapter = adapter_class()  # Create an instance of the adapter

    if fetch_all:
        raw_data_list = await adapter.fetch_all_data()
        if raw_data_list is not None:
            normalized_data = adapter.normalize_all_data(raw_data_list['data'] if 'data' in raw_data_list else raw_data_list)
            print(normalized_data)
            print(f"Number of items fetched from {adapter_class.__name__}: {len(normalized_data)}")
        else:
            print(f"No data fetched from {adapter_class.__name__}.")
    else:
        normalized_symbols = [symbol_normalization_func(symbol) for symbol in top_symbols]
        tasks = [fetch_and_normalize_data(adapter_class(symbol)) for symbol in normalized_symbols]
        normalized_data_list = await asyncio.gather(*tasks)

        successful_fetches = sum(1 for data in normalized_data_list if data is not None)

        print(f"Number of successful fetches: {successful_fetches}")
        for normalized_data in normalized_data_list:
            if normalized_data:
                print(f"{adapter_class.__name__} Normalized Data:", normalized_data)

async def main():
    """Run tests for multiple adapters."""
    print("Fetching top cryptocurrencies...")
    top_symbols = fetch_top_cryptos()  # Fetch top cryptocurrencies once

    # List of adapters and their respective symbol normalization functions
    adapters_info = [
        (BinanceAdapter, lambda s: s.replace('/', ''), True),   # Test fetch_all_data first
        (CoinbaseAdapter, lambda s: s.replace('/', '-'), True), # Test fetch_all_data first
        (KrakenAdapter, lambda s: s.replace('/', ''), True),
        (KuCoinAdapter, lambda s: s.replace('/', '-'), True),
        (BybitAdapter, lambda s: s.replace('/', ''), True),    # Add BybitAdapter to the test suite
        (HuobiAdapter, lambda s: s.replace('/', ''), True),     # Add HuobiAdapter to the test suite
        (BitfinexAdapter, lambda s: 't' + s.replace('/', ''), True),
    ]

    # Run tests for each adapter
    for adapter_class, symbol_normalization_func, fetch_all in adapters_info:
        await test_adapter(adapter_class, top_symbols, symbol_normalization_func, fetch_all)
        # Adding a delay to prevent rate limiting
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
