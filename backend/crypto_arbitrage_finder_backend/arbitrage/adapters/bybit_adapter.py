import aiohttp  # Ensure aiohttp is installed

class BybitAdapter:
    def __init__(self, symbol=None, category="spot"):
        self.exchangeName = "Bybit"
        self.symbol = symbol
        self.category = category
        self.api_url = 'https://api.bybit.com/v5/market/tickers'  # Bybit endpoint for ticker data
        # Add known quote currencies for Bybit
        self.quote_currencies = ['USDT', 'BTC', 'ETH', 'BUSD', 'USD', 'BNB', 'USDC', 'TUSD', 'XRP', 'TRX', 'RUB', 'GBP', 'EUR', 'JPY']

    async def fetch_data(self):
        """Fetch market data for a specific symbol from Bybit asynchronously."""
        params = {'category': self.category}
        if self.symbol:
            params['symbol'] = self.symbol
        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_url, params=params) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"Error fetching data for {self.symbol} from Bybit: {response.status}")
                    return None

    async def fetch_all_data(self):
        """Fetch all ticker data from Bybit asynchronously for the specified category."""
        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_url, params={'category': self.category}) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"Error fetching all ticker data from Bybit: {response.status}")
                    return None

    def normalize_data(self, raw_data):
        """Normalize the fetched data for a specific symbol from Bybit."""
        if raw_data and 'result' in raw_data and 'list' in raw_data['result'] and raw_data['result']['list']:
            data = raw_data['result']['list'][0]
            return {
                'symbol': self.format_symbol(data['symbol']),
                'price': float(data['lastPrice']),
                'high': float(data['highPrice']),
                'low': float(data['lowPrice']),
                'volume': float(data['volume24h']),
            }
        return None

    def normalize_all_data(self, raw_data):
        """Normalize the fetched data for all tickers from Bybit."""
        normalized_data = []
        if raw_data and 'result' in raw_data and 'list' in raw_data['result']:
            for data in raw_data['result']['list']:
                normalized_entry = {
                    'symbol': self.format_symbol(data['symbol']),
                    'price': float(data['lastPrice']),
                    'high': float(data['highPrice24h']),
                    'low': float(data['lowPrice24h']),
                    'volume': float(data['volume24h']),
                }
                normalized_data.append(normalized_entry)
        return normalized_data

    def format_symbol(self, symbol):
        """Format the symbol as BASE/QUOTE using known quote currencies."""
        quote = next((q for q in self.quote_currencies if symbol.endswith(q)), None)
        if quote:
            base = symbol.replace(quote, '')
            return f"{base}/{quote}"
        return symbol  # Return the original symbol if quote currency not found

