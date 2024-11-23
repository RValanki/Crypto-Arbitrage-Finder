import ccxt  # Ensure you have ccxt installed
from abc import ABC, abstractmethod  # Importing ABC and abstractmethod

class ExchangeAdapter(ABC):
    """Base class for exchange adapters. All adapters must implement fetch_data and normalize_data."""

    def __init__(self):
        self.exchangeName = ""
        self.makerFee = 0
        self.takerFee = 0

    @abstractmethod
    def fetch_data(self):
        """Fetch raw data from the exchange."""
        pass
    
    @abstractmethod
    def fetch_all_data(self):
        """Fetch raw data from the exchange."""
        pass

    @abstractmethod
    def normalize_data(self, raw_data):
        """Normalize the raw data into a consistent format."""
        pass
    
    @abstractmethod
    def normalize_all_data(self, raw_data):
        """Normalize the raw data into a consistent format."""
        pass

    @abstractmethod
    def format_symbol(self, raw_data):
        """Normalize the raw data into a consistent format."""
        pass
