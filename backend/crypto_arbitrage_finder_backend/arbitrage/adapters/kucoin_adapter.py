import aiohttp  # Ensure aiohttp is installed

class KuCoinAdapter:
    def __init__(self, symbol=None):
        self.symbol = symbol
        self.api_url = 'https://api.kucoin.com/api/v1/market/allTickers'  # Endpoint for all tickers data

    async def fetch_data(self):
        """Fetch market data for a specific symbol from KuCoin asynchronously."""
        if self.symbol:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.api_url) as response:
                    if response.status == 200:
                        data = await response.json()
                        # Filter for the specific symbol in the 'ticker' list
                        for ticker in data['data']['ticker']:
                            if ticker['symbol'] == self.symbol:
                                return ticker
                    else:
                        print(f"Error fetching data for {self.symbol} from KuCoin: {response.status}")
        return None

    async def fetch_all_data(self):
        """Fetch all ticker data from KuCoin asynchronously."""
        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_url) as response:
                if response.status == 200:
                    return await response.json()  # Return the full JSON response
                else:
                    print(f"Error fetching all ticker data from KuCoin: {response.status}")
                    return None

    def normalize_data(self, raw_data):
        """Normalize the fetched data for a specific symbol from KuCoin."""
        if raw_data:
            return {
                'symbol': raw_data['symbol'],
                'price': float(raw_data['last']),
                'high': float(raw_data['high']),
                'low': float(raw_data['low']),
                'volume': float(raw_data['vol']),
            }
        return None

    def normalize_all_data(self, raw_data):
        """Normalize the fetched data for all tickers from KuCoin."""
        print("hi")
        normalized_data = []
        if raw_data and 'ticker' in raw_data:
            print("hi3")
            for ticker in raw_data['ticker']:
                normalized_entry = {
                    'symbol': ticker['symbol'],
                    'price': float(ticker['last']),
                    'high': float(ticker['high']),
                    'low': float(ticker['low']),
                    'volume': float(ticker['vol']),
                }
                normalized_data.append(normalized_entry)
        return normalized_data
