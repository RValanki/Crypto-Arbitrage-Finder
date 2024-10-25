import aiohttp  # Ensure aiohttp is installed

class KrakenAdapter:
    def __init__(self, symbol=None):
        self.symbol = symbol
        self.api_url = 'https://api.kraken.com/0/public/Ticker'  # Endpoint for ticker information

    async def fetch_data(self):
        """Fetch market data from Kraken asynchronously."""
        if self.symbol:
            params = {'pair': self.symbol}  # Kraken uses 'pair' parameter
            async with aiohttp.ClientSession() as session:
                async with session.get(self.api_url, params=params) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        print(f"Error fetching data for {self.symbol} from Kraken: {response.status}")
                        return None
        return None

    def normalize_data(self, raw_data):
        """Normalize the fetched data from Kraken."""
        if raw_data and 'result' in raw_data:
            # Extracting the key for the symbol from the result
            result_key = list(raw_data['result'].keys())[0]  # Get the first pair key
            ticker_info = raw_data['result'][result_key]
            return {
                'symbol': result_key,
                'price': float(ticker_info['c'][0]),  # Current price (last trade closed)
                'high': float(ticker_info['h'][0]),    # Today's high price
                'low': float(ticker_info['l'][0]),     # Today's low price
                'volume': float(ticker_info['v'][1]),  # 24h volume
            }
        return None
