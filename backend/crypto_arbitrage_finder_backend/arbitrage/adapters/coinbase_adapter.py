import aiohttp  # Ensure aiohttp is installed

class CoinbaseAdapter:
    def __init__(self, symbol=None):
        self.symbol = symbol
        self.api_url = 'https://api.coinbase.com/v2/prices'

    async def fetch_data(self):
        """Fetch market data for a specific symbol from Coinbase asynchronously."""
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.api_url}/{self.symbol}/spot') as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"Error fetching data for {self.symbol}: {response.status}")
                    return None

    async def fetch_all_data(self):
        """Fetch all available ticker data from Coinbase asynchronously."""
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.api_url}/USDT/spot') as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"Error fetching all data: {response.status}")
                    return None

    def normalize_data(self, raw_data):
        """Normalize the fetched data for a specific symbol from Coinbase."""
        if raw_data:
            return {
                'symbol': f'{self.symbol}',
                'price': float(raw_data['data']['amount']),
            }
        return None

    def normalize_all_data(self, raw_data_list):
        """Normalize the fetched data for all tickers from Coinbase."""
        normalized_data = []
        for raw_data in raw_data_list:
            normalized_entry = {
                'symbol': raw_data['base'],
                'price': float(raw_data['amount']),
            }
            normalized_data.append(normalized_entry)
        return normalized_data
