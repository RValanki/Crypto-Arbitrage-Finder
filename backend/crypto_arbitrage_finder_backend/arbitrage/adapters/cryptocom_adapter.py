import aiohttp  # Make sure you have aiohttp installed

class CryptoComAdapter:
    def __init__(self, symbol=None):
        self.symbol = symbol
        self.api_url = 'https://api.crypto.com/v2/public/get-price'  # API endpoint for price data

    async def fetch_data(self):
        """Fetch market data from Crypto.com asynchronously."""
        async with aiohttp.ClientSession() as session:
            # Create the request parameters
            params = {
                'instrument_name': self.symbol,  # e.g., 'BTC_USDT'
            }
            async with session.get(self.api_url, params=params) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"Error fetching data for {self.symbol}: {response.status}")
                    return None

    def normalize_data(self, raw_data):
        """Normalize the fetched data."""
        if raw_data and 'result' in raw_data and raw_data['result']:
            return {
                'symbol': self.symbol.replace('_', '/'),  # Format correctly as Base/Quote
                'price': float(raw_data['result']['data']['last_price']),  # Extract the last price
            }
        return None
