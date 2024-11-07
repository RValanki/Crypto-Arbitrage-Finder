import aiohttp  # Ensure aiohttp is installed
import asyncio

class BinanceAdapter:
    def __init__(self, symbol=None):
        self.symbol = symbol
        self.api_url = 'https://api.binance.com/api/v3/ticker/24hr'  # Endpoint for 24hr ticker price change statistics
        self.quote_currencies = ['BTC', 'ETH', 'USDT', 'BUSD', 'USDC', 'FDUSD', 'USD', 'BNB', 'PAX', 'TUSD', 'XRP', 'NGN', 'TRX', 'RUB', 'TRY', 'EUR', 'ZAR', 'KRW', 'IDRT', 'BIDR', 'AUD', 'DAI', 'BRL', 'RUB', 'BVND', 'GBP', 'BRL', 'UAH', 'COPS', 'XBT', 'CHF', 'CAD', 'JPY']

    async def fetch_data(self):
        """Fetch market data for a specific symbol from Binance asynchronously."""
        if self.symbol:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.api_url, params={'symbol': self.symbol}) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        print(f"Error fetching data for {self.symbol} from Binance: {response.status}")
                        return None
        return None

    async def fetch_all_data(self):
        """Fetch all ticker data from Binance asynchronously."""
        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"Error fetching all ticker data from Binance: {response.status}")
                    return None

    def normalize_data(self, raw_data):
        """Normalize the fetched data for a specific symbol from Binance."""
        if raw_data:
            formatted_symbol = self.format_symbol(raw_data['symbol'])
            return {
                'symbol': formatted_symbol,
                'price': float(raw_data['lastPrice']),
                'high': float(raw_data['highPrice']),
                'low': float(raw_data['lowPrice']),
                'volume': float(raw_data['volume']),
            }
        return None

    def normalize_all_data(self, raw_data_list):
        """Normalize the fetched data for all tickers from Binance."""
        normalized_data = []
        for raw_data in raw_data_list:
            formatted_symbol = self.format_symbol(raw_data['symbol'])
            normalized_entry = {
                'symbol': formatted_symbol,
                'price': float(raw_data['lastPrice']),
                'high': float(raw_data['highPrice']),
                'low': float(raw_data['lowPrice']),
                'volume': float(raw_data['volume']),
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

    async def save_all_normalized_data_to_file(self, file_path):
        """Fetch, normalize, and save data for all tickers to a text file."""
        raw_data_list = await self.fetch_all_data()
        normalized_data_list = self.normalize_all_data(raw_data_list)
        if normalized_data_list:
            with open(file_path, 'w') as file:
                for data in normalized_data_list:
                    file.write(str(data) + "\n")
            print(f"All normalized data saved to {file_path}")
        else:
            print("No data to save.")

# Example usage:
async def main():
    all_adapter = BinanceAdapter()
    await all_adapter.save_all_normalized_data_to_file("all_ticker_data.txt")

# Run the main function
asyncio.run(main())
