import aiohttp  # Ensure aiohttp is installed

class KuCoinAdapter:
    def __init__(self, symbol=None):
        self.symbol = symbol
        self.api_url = 'https://api.kucoin.com/api/v1/market/orderbook/level1'  # Endpoint for latest order book level 1 data

    async def fetch_data(self):
        """Fetch market data from KuCoin asynchronously."""
        if self.symbol:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.api_url, params={'symbol': self.symbol}) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        print(f"Error fetching data for {self.symbol} from KuCoin: {response.status}, {await response.text()}")
                        return None
        return None

    def normalize_data(self, raw_data):
        """Normalize the fetched data from KuCoin."""
        if raw_data and 'data' in raw_data:
            data = raw_data['data']
            return {
                'symbol': self.symbol,
                'price': float(data['price']),   # Current price
                'high': float(data.get('high', 0)),  # High price, default to 0 if not present
                'low': float(data.get('low', 0)),    # Low price, default to 0 if not present
                'volume': float(data.get('size', 0)), # Volume, default to 0 if not present
            }
        return None
