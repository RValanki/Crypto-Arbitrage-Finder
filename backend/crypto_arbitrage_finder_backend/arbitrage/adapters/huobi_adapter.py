import aiohttp  # Ensure aiohttp is installed

class HuobiAdapter:
    def __init__(self, symbol=None):
        self.symbol = symbol
        self.api_url = 'https://api.huobi.pro/v1/common/symbols'  # Endpoint for symbol information
        self.ticker_url = 'https://api.huobi.pro/market/tickers'  # Endpoint for ticker data

    async def fetch_data(self):
        """Fetch market data for a specific symbol from Huobi asynchronously."""
        if self.symbol:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.ticker_url) as response:
                    if response.status == 200:
                        data = await response.json()
                        normalized_data = self.normalize_data(data)
                        return normalized_data
                    else:
                        print(f"Error fetching data for {self.symbol} from Huobi: {response.status}")
                        return None
        return None

    async def fetch_all_data(self):
        """Fetch all ticker data from Huobi asynchronously."""
        async with aiohttp.ClientSession() as session:
            async with session.get(self.ticker_url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"Error fetching all ticker data from Huobi: {response.status}")
                    return None

    def normalize_data(self, raw_data):
        """Normalize the fetched data for a specific symbol from Huobi."""
        if raw_data and 'data' in raw_data:
            for entry in raw_data['data']:
                if entry['symbol'] == self.symbol:
                    return {
                        'symbol': entry['symbol'],
                        'price': float(entry['close']),
                        'high': float(entry['high']),
                        'low': float(entry['low']),
                        'volume': float(entry['amount']),
                    }
        return None

    def normalize_all_data(self, raw_data):
        """Normalize the fetched data for all tickers from Huobi."""
        normalized_data = []
        print(raw_data)
        print("mao")
        if raw_data:
            for data in raw_data:
                normalized_entry = {
                    'symbol': data['symbol'],
                    'price': float(data['close']),
                    'high': float(data['high']),
                    'low': float(data['low']),
                    'volume': float(data['amount']),
                }
                normalized_data.append(normalized_entry)
        return normalized_data
