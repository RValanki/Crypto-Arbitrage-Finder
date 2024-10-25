import aiohttp  # Ensure aiohttp is installed

class KrakenAdapter:
    def __init__(self, symbol=None):
        self.symbol = symbol
        self.api_url = 'https://api.kraken.com/0/public/Ticker'  # Endpoint for ticker information

    async def fetch_data(self):
        """Fetch market data for a specific symbol from Kraken asynchronously."""
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

    async def fetch_all_data(self):
        """Fetch all market data from Kraken asynchronously."""
        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_url) as response:  # Use the same URL to get all tickers
                if response.status == 200:
                    all_ticker_data = await response.json()
                    if 'result' in all_ticker_data:
                        normalized_data = []
                        for ticker_key in all_ticker_data['result']:
                            self.symbol = ticker_key  # Set the current pair key
                            normalized_data.append(self.normalize_data(all_ticker_data))  # Normalize data for each ticker
                        return normalized_data
                else:
                    print(f"Error fetching all tickers from Kraken: {response.status}")
                    return None

    def normalize_data(self, raw_data):
        """Normalize the fetched data from Kraken."""
        if raw_data and 'result' in raw_data:
            ticker_info = raw_data['result'][self.symbol]  # Access data for the current symbol
            return {
                'symbol': self.symbol,
                'price': float(ticker_info['c'][0]),  # Current price (last trade closed)
                'high': float(ticker_info['h'][0]),    # Today's high price
                'low': float(ticker_info['l'][0]),     # Today's low price
                'volume': float(ticker_info['v'][1]),  # 24h volume
            }
        return None

    def normalize_all_data(self, raw_data):
        """Normalize all ticker data returned from Kraken."""
        normalized_data = []
        for item in raw_data:
            normalized_data.append(self.normalize_data(item))
        return normalized_data
