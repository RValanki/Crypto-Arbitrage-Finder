import asyncio
from adapters.binance_adapter import BinanceAdapter  # Importing the BinanceAdapter class
from adapters.coinbase_adapter import CoinbaseAdapter

async def fetch_binance_data(adapter):
    raw_data = await adapter.fetch_data()  # Fetch raw data asynchronously
    return adapter.normalize_data(raw_data)

async def test_binance_adapter_multiple_cryptos():
    # Top 20 cryptocurrencies by market cap (validated for Binance)
    top_symbols = [
        'BTC/USDT', 'ETH/USDT', 'BNB/USDT', 'XRP/USDT', 'ADA/USDT',
        'SOL/USDT', 'DOGE/USDT', 'DOT/USDT', 'MATIC/USDT', 'TRX/USDT',
        'LTC/USDT', 'AVAX/USDT', 'LINK/USDT', 'FIL/USDT', 'ETC/USDT',
        'ALGO/USDT', 'VET/USDT', 'CHZ/USDT', 'SAND/USDT', 'FLOKI/USDT',
    ]

    tasks = [fetch_binance_data(BinanceAdapter(symbol)) for symbol in top_symbols]
    normalized_data_list = await asyncio.gather(*tasks)

    for normalized_data in normalized_data_list:
        print("Binance Normalized Data:", normalized_data)

async def fetch_coinbase_data(adapter):
    raw_data = await adapter.fetch_data()
    return adapter.normalize_data(raw_data)

async def test_coinbase_adapter_multiple_cryptos():
    # Top 20 cryptocurrencies by market cap (hardcoded for Coinbase)
    top_symbols = [
        'BTC-USDT', 'ETH-USDT', 'LTC-USDT', 'BCH-USDT', 'XRP-USDT',
        'AVAX-USDT', 'LINK-USDT', 'MATIC-USDT', 'SOL-USDT', 'DOT-USDT',
        'DOGE-USDT', 'SHIB-USDT', 'TRX-USDT', 'VET-USDT', 'CRO-USDT',
        'ALGO-USDT', 'XLM-USDT', 'FIL-USDT', 'SAND-USDT', 'FLOKI-USDT',
    ]

    tasks = [fetch_coinbase_data(CoinbaseAdapter(symbol)) for symbol in top_symbols]
    normalized_data_list = await asyncio.gather(*tasks)

    for normalized_data in normalized_data_list:
        print("Coinbase Normalized Data:", normalized_data)

if __name__ == "__main__":
    print("Testing Binance Adapter for multiple cryptocurrencies...")
    asyncio.run(test_binance_adapter_multiple_cryptos())
    print("\nTesting Coinbase Adapter for multiple cryptocurrencies...")
    asyncio.run(test_coinbase_adapter_multiple_cryptos())
