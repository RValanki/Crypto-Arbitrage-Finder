import aiohttp  # Ensure aiohttp is installed
import asyncio

class BitfinexAdapter:
    def __init__(self):
        self.exchangeName = "Bitfinex"
        self.makerFee = 0.001
        self.takerFee = 0.002
        self.api_url = 'https://api-pub.bitfinex.com/v2/tickers?symbols=ALL'  # Hardcoded endpoint for all ticker data
        self.quote_currencies = ['BTC', 'ETH', 'USDT', 'BUSD', 'USDC', 'FDUSD', 'USD', 'BNB', 'PAX', 'TUSD', 'XRP', 'NGN', 'TRX', 'RUB', 'TRY', 'EUR', 'ZAR', 'KRW', 'IDRT', 'BIDR', 'AUD', 'DAI', 'BRL', 'RUB', 'BVND', 'GBP', 'BRL', 'UAH', 'COPS', 'XBT', 'CHF', 'CAD', 'JPY', 'USD', 'USDT', 'BTC', 'ETH', 'EUR', 'JPY', 'GBP', 'CHF', 'XRP', 'TRX', 'BCH', 'LTC', 'UST']

    async def fetch_data(self, symbol):
        """Fetch market data for a specific symbol from Bitfinex asynchronously."""
        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_url) as response:
                if response.status == 200:
                    raw_data = await response.json()
                    return self.normalize_data(raw_data, symbol)
                else:
                    print(f"Error fetching data for {symbol} from Bitfinex: {response.status}")
                    return None

    async def fetch_all_data(self):
        """Fetch all ticker data from Bitfinex asynchronously."""
        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_url) as response:
                if response.status == 200:
                    raw_data = await response.json()
                    return self.normalize_all_data(raw_data)
                else:
                    print(f"Error fetching all ticker data from Bitfinex: {response.status}")
                    return None

    def normalize_data(self, raw_data, symbol):
        """Normalize the fetched data for a specific symbol from Bitfinex."""
        if raw_data:
            for entry in raw_data:
                if entry[0] == f't{symbol}':  # Check the symbol
                    try:
                        return {
                            'symbol': self.format_symbol(entry[0]),  # Formatted symbol (e.g., "BTC/USD")
                            'price': float(entry[1]),  # Last price
                            'high': float(entry[7]),  # High price
                            'low': float(entry[8]),   # Low price
                            'volume': float(entry[9]),  # 24h volume
                        }
                    except (IndexError, ValueError) as e:
                        print(f"Error normalizing data for {entry}: {e}")
        return None

    def normalize_all_data(self, raw_data_list):
        """Normalize the fetched data for all tickers from Bitfinex."""
        normalized_data = []
        for raw_data in raw_data_list:
            try:
                if isinstance(raw_data, dict):
                    # When data is in a dictionary format
                    normalized_data.append({
                        'symbol': self.format_symbol(raw_data.get('symbol')),  # Format symbol to BASE/QUOTE
                        'price': float(raw_data.get('price', -1)),  # Use -1 as a default if price is missing
                        'high': float(raw_data.get('high', -1)),
                        'low': float(raw_data.get('low', -1)),
                        'volume': float(raw_data.get('volume', -1)),
                    })
                elif isinstance(raw_data, list) and len(raw_data) > 9:
                    # When data is in a list format with expected indices
                    normalized_data.append({
                        'symbol': self.format_symbol(raw_data[0]),  # Format symbol to BASE/QUOTE
                        'price': float(raw_data[1]),  # Last price
                        'high': float(raw_data[7]),  # High price
                        'low': float(raw_data[8]),   # Low price
                        'volume': float(raw_data[9]),  # 24h volume
                    })
                else:
                    print(f"Unrecognized data format for {raw_data}")

            except (IndexError, ValueError, TypeError) as e:
                print(f"Error normalizing data for {raw_data}: {e}")
        
        return normalized_data

    def format_symbol(self, symbol):
        """Format the symbol as BASE/QUOTE using known quote currencies."""
        # Bitfinex symbols typically start with 't' followed by the base and quote currency (e.g., 'tBTCUSD')
        if symbol.startswith('t'):
            symbol = symbol[1:]  # Remove the 't' prefix
        # Define known quote currencies
        for quote in self.quote_currencies:
            if symbol.endswith(quote):
                base = symbol.replace(quote, '')
                return f"{base}/{quote}"
        return symbol  # Return the original symbol if quote currency not found

