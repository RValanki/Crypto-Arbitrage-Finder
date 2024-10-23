import aiohttp  # Make sure you have aiohttp installed

class CoinbaseAdapter:
    def __init__(self, symbol=None):
        self.symbol = symbol
        self.api_url = 'https://api.coinbase.com/v2/prices'

    async def fetch_data(self):
        # Fetch market data from Coinbase asynchronously
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.api_url}/{self.symbol}/spot') as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"Error fetching data for {self.symbol}: {response.status}")
                    return None

    def normalize_data(self, raw_data):
        # Normalize the fetched data
        if raw_data:
            # Split the symbol using '-'
            base_currency, quote_currency = self.symbol.split('-')
            return {
                'symbol': f'{base_currency}/{quote_currency}',  # Format correctly as Base/Quote
                'price': float(raw_data['data']['amount']),
            }
        return None
