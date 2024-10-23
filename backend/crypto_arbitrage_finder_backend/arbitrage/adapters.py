# arbitrage/test.py

import ccxt  # Ensure you have ccxt installed
from abc import ABC, abstractmethod  # Importing ABC and abstractmethod

class ExchangeAdapter(ABC):
    """Base class for exchange adapters. All adapters must implement fetch_data and normalize_data."""

    @abstractmethod
    def fetch_data(self):
        """Fetch raw data from the exchange."""
        pass

    @abstractmethod
    def normalize_data(self, raw_data):
        """Normalize the raw data into a consistent format."""
        pass

class BinanceAdapter(ExchangeAdapter):
    """Adapter for the Binance exchange."""

    def __init__(self, symbol='BTC/USDT'):
        self.exchange = ccxt.binance()  # Initialize the Binance exchange
        self.symbol = symbol

    def fetch_data(self):
        """Fetch raw market data from Binance."""
        try:
            ticker = self.exchange.fetch_ticker(self.symbol)
            return ticker
        except Exception as e:
            print(f"Error fetching data from Binance: {e}")
            return None

    def normalize_data(self, raw_data):
        """Normalize the raw market data into a consistent format."""
        if raw_data is None:
            return None

        normalized_data = {
            'symbol': raw_data.get('symbol', self.symbol),  # Default to self.symbol if not present
            'price': raw_data.get('last'),                  # Last trade price
            'bid': raw_data.get('bid'),                      # Highest bid
            'ask': raw_data.get('ask'),                      # Lowest ask
            'timestamp': raw_data.get('timestamp'),          # Timestamp of the data
        }
        return normalized_data

def test_binance_adapter():
    adapter = BinanceAdapter(symbol='BTC/USDT')
    
    raw_data = adapter.fetch_data()
    normalized_data = adapter.normalize_data(raw_data)
    
    print("Raw Data:", raw_data)
    print("Normalized Data:", normalized_data)

    # Add assertions to validate the output
    assert raw_data is not None, "Raw data should not be None"
    assert normalized_data is not None, "Normalized data should not be None"
    assert normalized_data['symbol'] == 'BTC/USDT', "Symbol should be BTC/USDT"
    assert 'price' in normalized_data, "Normalized data should contain price"

if __name__ == "__main__":
    test_binance_adapter()
