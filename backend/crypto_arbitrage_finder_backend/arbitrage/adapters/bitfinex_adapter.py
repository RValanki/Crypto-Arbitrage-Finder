import aiohttp

class BitfinexAdapter:
    """Adapter for fetching data from Bitfinex."""
    
    def __init__(self, symbol):
        self.symbol = symbol

    async def fetch_data(self):
        """Fetch raw data from Bitfinex API."""
        url = f'https://api.bitfinex.com/v2/tickers?symbols={self.symbol}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"Error fetching data from Bitfinex: {response.status}")
                    return None

    def normalize_data(self, raw_data):
        """Normalize the raw data returned from Bitfinex."""
        # Example normalization logic; adjust as necessary
        if raw_data:
            return {
                'symbol': self.symbol,
                'price': raw_data[0][6],  # Price is at index 6 in the Bitfinex response
                'volume': raw_data[0][7],  # Volume is at index 7
            }
        return None
