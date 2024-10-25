import asyncio
import requests
from adapters.binance_adapter import BinanceAdapter  # Adjust the import according to your project structure
from adapters.coinbase_adapter import CoinbaseAdapter
from adapters.kraken_adapter import KrakenAdapter
from adapters.bitfinex_adapter import BitfinexAdapter
from adapters.kucoin_adapter import KuCoinAdapter

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

async def test_adapter_multiple_cryptos(adapter_class, top_symbols, symbol_normalization_func):
    """Test a specific adapter with multiple cryptocurrencies."""
    normalized_symbols = [symbol_normalization_func(symbol) for symbol in top_symbols]
    tasks = [fetch_and_normalize_data(adapter_class(symbol)) for symbol in normalized_symbols]
    normalized_data_list = await asyncio.gather(*tasks)

    successful_fetches = sum(1 for data in normalized_data_list if data is not None)

    print(f"Number of successful fetches: {successful_fetches}")
    for normalized_data in normalized_data_list:
        if normalized_data:
            print(f"{adapter_class.__name__} Normalized Data:", normalized_data)

async def test_fetch_all_binance_data():
    """Test fetching all ticker data from Binance and print the number of items."""
    print("Testing fetch_all_data method for Binance Adapter...")
    adapter = BinanceAdapter()
    raw_data_list = await adapter.fetch_all_data()
    if raw_data_list is not None:
        # Normalize the fetched data
        normalized_data = adapter.normalize_all_data(raw_data_list)
        print(f"Number of items fetched from Binance: {len(normalized_data)}")
        print(normalized_data)
    else:
        print("No data fetched from Binance.")

async def main():
    """Run tests for Binance, Coinbase, Kraken, Bitfinex, and KuCoin adapters."""
    print("Fetching top cryptocurrencies...")
    top_symbols = fetch_top_cryptos()  # Fetch top cryptocurrencies once

    # Test fetching all data from Binance
    await test_fetch_all_binance_data()

    print("Testing Binance Adapter for top 200 cryptocurrencies...")
    await test_adapter_multiple_cryptos(BinanceAdapter, top_symbols, lambda s: s.replace('/', ''))

    # Adding a delay to prevent rate limiting
    await asyncio.sleep(1)

    print("\nTesting Coinbase Adapter for top 200 cryptocurrencies...")
    await test_adapter_multiple_cryptos(CoinbaseAdapter, top_symbols, lambda s: s.replace('/', '-'))

    # Adding a delay to prevent rate limiting
    await asyncio.sleep(1)

    print("\nTesting Kraken Adapter for top 200 cryptocurrencies...")
    await test_adapter_multiple_cryptos(KrakenAdapter, top_symbols, lambda s: s.replace('/', ''))

    # Adding a delay to prevent rate limiting
    await asyncio.sleep(1)

    print("\nTesting Bitfinex Adapter for top 200 cryptocurrencies...")
    await test_adapter_multiple_cryptos(BitfinexAdapter, top_symbols, lambda s: 't' + s.replace('/', ''))

    # Adding a delay to prevent rate limiting
    await asyncio.sleep(1)

    print("\nTesting KuCoin Adapter for top 200 cryptocurrencies...")
    await test_adapter_multiple_cryptos(KuCoinAdapter, top_symbols, lambda s: s.replace('/', '-'))

if __name__ == "__main__":
    asyncio.run(main())
