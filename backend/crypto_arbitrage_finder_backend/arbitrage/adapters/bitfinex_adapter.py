import aiohttp

class BitfinexAdapter:
    """Adapter for fetching data from Bitfinex."""
    
    def __init__(self, symbol=None):
        self.symbol = symbol

    async def fetch_data(self):
        """Fetch raw data for a specific symbol from Bitfinex API."""
        url = f'https://api.bitfinex.com/v2/tickers?symbols={self.symbol}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"Error fetching data from Bitfinex: {response.status}")
                    return None

    async def fetch_all_data(self):
        """Fetch all ticker data from Bitfinex API."""
        url = 'https://api.bitfinex.com/v2/tickers'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"Error fetching all data from Bitfinex: {response.status}")
                    return None

    def normalize_data(self, raw_data):
        """Normalize the raw data returned from Bitfinex."""
        if raw_data:
            return {
                'symbol': self.symbol,
                'price': raw_data[0][6],  # Price is at index 6 in the Bitfinex response
                'volume': raw_data[0][7],  # Volume is at index 7
            }
        return None

    def normalize_all_data(self, raw_data):
        """Normalize all ticker data returned from Bitfinex."""
        normalized_data = []
        for item in raw_data:
            normalized_data.append({
                'symbol': item[0],
                'price': item[6],  # Price is at index 6
                'volume': item[7],  # Volume is at index 7
            })
        return normalized_data
