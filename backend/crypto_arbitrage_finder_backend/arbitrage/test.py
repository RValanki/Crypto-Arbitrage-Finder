import asyncio
import requests
from adapters.binance_adapter import BinanceAdapter  # Importing the BinanceAdapter class
from adapters.coinbase_adapter import CoinbaseAdapter  # Importing the CoinbaseAdapter class
from adapters.kraken_adapter import KrakenAdapter  # Importing the KrakenAdapter class
from adapters.bitfinex_adapter import BitfinexAdapter  # Importing the BitfinexAdapter class

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

async def fetch_binance_data(adapter):
    """Fetch and normalize data from Binance for a given adapter."""
    try:
        raw_data = await adapter.fetch_data()  # Fetch raw data asynchronously
        if raw_data:
            return adapter.normalize_data(raw_data)
        else:
            print(f"No data returned for {adapter.symbol} from Binance.")
            return None
    except Exception as e:
        print(f"Error fetching data for {adapter.symbol} from Binance: {e}")
        return None  # Return None on error

async def test_binance_adapter_multiple_cryptos(top_symbols):
    """Test Binance adapter with multiple cryptocurrencies."""
    # Normalize symbols for Binance by removing '/'
    normalized_symbols = [symbol.replace('/', '') for symbol in top_symbols]

    tasks = [fetch_binance_data(BinanceAdapter(symbol)) for symbol in normalized_symbols]
    normalized_data_list = await asyncio.gather(*tasks)

    successful_fetches = sum(1 for data in normalized_data_list if data is not None)

    print(f"Number of successful fetches from Binance: {successful_fetches}")
    for normalized_data in normalized_data_list:
        if normalized_data:
            print("Binance Normalized Data:", normalized_data)

async def fetch_coinbase_data(adapter):
    """Fetch and normalize data from Coinbase for a given adapter."""
    try:
        raw_data = await adapter.fetch_data()
        if raw_data:
            return adapter.normalize_data(raw_data)
        else:
            print(f"No data returned for {adapter.symbol} from Coinbase.")
            return None
    except Exception as e:
        print(f"Error fetching data for {adapter.symbol} from Coinbase: {e}")
        return None  # Return None on error

async def test_coinbase_adapter_multiple_cryptos(top_symbols):
    """Test Coinbase adapter with multiple cryptocurrencies."""
    tasks = [fetch_coinbase_data(CoinbaseAdapter(symbol.replace('/', '-'))) for symbol in top_symbols]
    normalized_data_list = await asyncio.gather(*tasks)

    successful_fetches = sum(1 for data in normalized_data_list if data is not None)

    print(f"Number of successful fetches from Coinbase: {successful_fetches}")
    for normalized_data in normalized_data_list:
        if normalized_data:
            print("Coinbase Normalized Data:", normalized_data)

async def fetch_kraken_data(adapter):
    """Fetch and normalize data from Kraken for a given adapter."""
    try:
        raw_data = await adapter.fetch_data()
        if raw_data:
            return adapter.normalize_data(raw_data)
        else:
            print(f"No data returned for {adapter.symbol} from Kraken.")
            return None
    except Exception as e:
        print(f"Error fetching data for {adapter.symbol} from Kraken: {e}")
        return None  # Return None on error

async def test_kraken_adapter_multiple_cryptos(top_symbols):
    """Test Kraken adapter with multiple cryptocurrencies."""
    # Normalize symbols for Kraken by removing '/'
    normalized_symbols = [symbol.replace('/', '') for symbol in top_symbols]

    tasks = [fetch_kraken_data(KrakenAdapter(symbol)) for symbol in normalized_symbols]
    normalized_data_list = await asyncio.gather(*tasks)

    successful_fetches = sum(1 for data in normalized_data_list if data is not None)

    print(f"Number of successful fetches from Kraken: {successful_fetches}")
    for normalized_data in normalized_data_list:
        if normalized_data:
            print("Kraken Normalized Data:", normalized_data)

async def fetch_bitfinex_data(adapter):
    """Fetch and normalize data from Bitfinex for a given adapter."""
    try:
        raw_data = await adapter.fetch_data()
        if raw_data:
            return adapter.normalize_data(raw_data)
        else:
            print(f"No data returned for {adapter.symbol} from Bitfinex.")
            return None
    except Exception as e:
        print(f"Error fetching data for {adapter.symbol} from Bitfinex: {e}")
        return None  # Return None on error

async def test_bitfinex_adapter_multiple_cryptos(top_symbols):
    """Test Bitfinex adapter with multiple cryptocurrencies."""
    # Normalize symbols for Bitfinex by adding 't' prefix and removing '/'
    normalized_symbols = ['t' + symbol.replace('/', '') for symbol in top_symbols]

    tasks = [fetch_bitfinex_data(BitfinexAdapter(symbol)) for symbol in normalized_symbols]
    normalized_data_list = await asyncio.gather(*tasks)

    successful_fetches = sum(1 for data in normalized_data_list if data is not None)

    print(f"Number of successful fetches from Bitfinex: {successful_fetches}")
    for normalized_data in normalized_data_list:
        if normalized_data:
            print("Bitfinex Normalized Data:", normalized_data)

async def main():
    """Run tests for Binance, Coinbase, Kraken, and Bitfinex adapters."""
    print("Fetching top cryptocurrencies...")
    top_symbols = fetch_top_cryptos()  # Fetch top cryptocurrencies once

    print("Testing Binance Adapter for top 200 cryptocurrencies...")
    await test_binance_adapter_multiple_cryptos(top_symbols)

    # Adding a delay to prevent rate limiting (you can adjust this if needed)
    await asyncio.sleep(1)

    print("\nTesting Coinbase Adapter for top 200 cryptocurrencies...")
    await test_coinbase_adapter_multiple_cryptos(top_symbols)

    # Adding a delay to prevent rate limiting
    await asyncio.sleep(1)

    print("\nTesting Kraken Adapter for top 200 cryptocurrencies...")
    await test_kraken_adapter_multiple_cryptos(top_symbols)

    # Adding a delay to prevent rate limiting
    await asyncio.sleep(1)

    print("\nTesting Bitfinex Adapter for top 200 cryptocurrencies...")
    await test_bitfinex_adapter_multiple_cryptos(top_symbols)

if __name__ == "__main__":
    asyncio.run(main())
