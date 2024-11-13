import aiohttp
import json  # For saving JSON data to file

class KuCoinAdapter:
    def __init__(self, symbol=None):
        self.symbol = symbol
        self.api_url = 'https://api.kucoin.com/api/v1/market/allTickers'  # Endpoint for all tickers data
        self.quote_currencies = ['BTC', 'ETH', 'USDT', 'BUSD', 'USDC', 'FDUSD', 'USD', 'BNB', 'PAX', 'TUSD', 'XRP', 'NGN', 
                                 'TRX', 'RUB', 'TRY', 'EUR', 'ZAR', 'KRW', 'IDRT', 'BIDR', 'AUD', 'DAI', 'BRL', 'RUB', 
                                 'BVND', 'GBP', 'BRL', 'UAH', 'COPS', 'XBT', 'CHF', 'CAD', 'JPY']

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

    def format_symbol(self, symbol):
        """Format the symbol as BASE/QUOTE using known quote currencies."""
        quote = next((q for q in self.quote_currencies if symbol.endswith(q)), None)
        if quote:
            base = symbol.replace(f"-{quote}", '')  # KuCoin uses a dash, e.g., "BTC-USDT"
            return f"{base}/{quote}"
        return symbol  # Return the original symbol if quote currency not found

    def normalize_data(self, raw_data):
        """Normalize the fetched data for a specific symbol from KuCoin."""
        if raw_data:
            formatted_symbol = self.format_symbol(raw_data['symbol'])
            return {
                'symbol': formatted_symbol,
                'price': float(raw_data['last']),
                'high': float(raw_data['high']),
                'low': float(raw_data['low']),
                'volume': float(raw_data['vol']),
            }
        return None

    def normalize_all_data(self, raw_data):
        """Normalize the fetched data for all tickers from KuCoin."""
        normalized_data = []
        if raw_data and 'ticker' in raw_data:
            for ticker in raw_data['ticker']:
                formatted_symbol = self.format_symbol(ticker['symbol'])
                normalized_entry = {
                    'symbol': formatted_symbol,
                    'price': float(ticker['last']) if ticker['last'] is not None else -1,
                    'high': float(ticker['high']),
                    'low': float(ticker['low']),
                    'volume': float(ticker['vol']),
                }
                normalized_data.append(normalized_entry)
        return normalized_data

    async def save_raw_data_to_file(self, raw_data, file_path="kucoin_raw_data.txt"):
        """Save the raw JSON data to a text file."""
        if raw_data:
            with open(file_path, 'w') as file:
                file.write(json.dumps(raw_data, indent=4))  # Format JSON data with indentation
            print(f"Raw data saved to {file_path}")
        else:
            print("No raw data to save.")
