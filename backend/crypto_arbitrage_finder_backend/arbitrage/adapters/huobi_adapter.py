import aiohttp  # Ensure aiohttp is installed

class HuobiAdapter:
    def __init__(self, symbol=None):
        self.symbol = symbol
        self.api_url = 'https://api.huobi.pro/v1/common/symbols'  # Endpoint for symbol information
        self.ticker_url = 'https://api.huobi.pro/market/tickers'  # Endpoint for ticker data
        self.quote_currencies = ['BTC', 'ETH', 'USDT', 'BUSD', 'USDC', 'FDUSD', 'USD', 'BNB', 'PAX', 'TUSD', 'XRP', 'NGN', 'TRX', 'RUB', 'TRY', 'EUR', 'ZAR', 'KRW', 'IDRT', 'BIDR', 'AUD', 'DAI', 'BRL', 'RUB', 'BVND', 'GBP', 'BRL', 'UAH', 'COPS', 'XBT', 'CHF', 'CAD', 'JPY', 'USDD']

    async def fetch_data(self):
        """Fetch market data for a specific symbol from Huobi asynchronously."""
        if self.symbol:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.ticker_url) as response:
                    if response.status == 200:
                        data = await response.json()
                        normalized_data = self.normalize_data(data)
                        return normalized_data
                    else:
                        print(f"Error fetching data for {self.symbol} from Huobi: {response.status}")
                        return None
        return None

    async def fetch_all_data(self):
        """Fetch all ticker data from Huobi asynchronously."""
        async with aiohttp.ClientSession() as session:
            async with session.get(self.ticker_url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"Error fetching all ticker data from Huobi: {response.status}")
                    return None

    def normalize_data(self, raw_data):
        """Normalize the fetched data for a specific symbol from Huobi."""
        if raw_data and 'data' in raw_data:
            for entry in raw_data['data']:
                if entry['symbol'] == self.symbol:
                    return {
                        'symbol': self.format_symbol(entry['symbol']),
                        'price': float(entry['close']),
                        'high': float(entry['high']),
                        'low': float(entry['low']),
                        'volume': float(entry['amount']),
                    }
        return None

    def normalize_all_data(self, raw_data):
        """Normalize the fetched data for all tickers from Huobi."""
        normalized_data = []
        if raw_data and 'data' in raw_data:
            for data in raw_data['data']:
                normalized_entry = {
                    'symbol': self.format_symbol(data['symbol'].upper()),
                    'price': float(data['close']),
                    'high': float(data['high']),
                    'low': float(data['low']),
                    'volume': float(data['amount']),
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

    async def save_all_normalized_data_to_file(self, file_path="huobi_normalized_data.txt"):
        """Fetch, normalize, and save data for all tickers to a text file."""
        raw_data = await self.fetch_all_data()
        if raw_data:
            normalized_data = self.normalize_all_data(raw_data)
            with open(file_path, 'w') as file:
                for entry in normalized_data:
                    file.write(f"{entry}\n")
            print(f"Normalized data saved to {file_path}")
        else:
            print("No data to save.")

# Example usage:
async def main():
    huobi_adapter = HuobiAdapter()  # Optionally pass a specific symbol, e.g., symbol="BTCUSDT"
    await huobi_adapter.save_all_normalized_data_to_file()

# Run the main function
import asyncio
asyncio.run(main())
