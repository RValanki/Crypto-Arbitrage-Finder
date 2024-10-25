import aiohttp  # Ensure aiohttp is installed

class BinanceAdapter:
    def __init__(self, symbol=None):
        self.symbol = symbol
        self.api_url = 'https://api.binance.com/api/v3/ticker/24hr'  # Endpoint for 24hr ticker price change statistics

    async def fetch_data(self):
        """Fetch market data for a specific symbol from Binance asynchronously."""
        if self.symbol:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.api_url, params={'symbol': self.symbol}) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        print(f"Error fetching data for {self.symbol} from Binance: {response.status}")
                        return None
        return None

    async def fetch_all_data(self):
        """Fetch all ticker data from Binance asynchronously."""
        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"Error fetching all ticker data from Binance: {response.status}")
                    return None

    def normalize_data(self, raw_data):
        """Normalize the fetched data for a specific symbol from Binance."""
        if raw_data:
            return {
                'symbol': raw_data['symbol'],
                'price': float(raw_data['lastPrice']),
                'high': float(raw_data['highPrice']),
                'low': float(raw_data['lowPrice']),
                'volume': float(raw_data['volume']),
            }
        return None

    def normalize_all_data(self, raw_data_list):
        """Normalize the fetched data for all tickers from Binance."""
        normalized_data = []
        for raw_data in raw_data_list:
            normalized_entry = {
                'symbol': raw_data['symbol'],
                'price': float(raw_data['lastPrice']),
                'high': float(raw_data['highPrice']),
                'low': float(raw_data['lowPrice']),
                'volume': float(raw_data['volume']),
            }
            normalized_data.append(normalized_entry)
        return normalized_data
