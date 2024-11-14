import aiohttp  # Ensure aiohttp is installed
import asyncio

class KrakenAdapter:
    def __init__(self):
        self.exchangeName = "Kraken"
        self.api_url = 'https://api.kraken.com/0/public/Ticker'  # Endpoint for ticker information
        # Known quote currencies
        self.quote_currencies = ['BTC', 'ETH', 'USDT', 'BUSD', 'USDC', 'FDUSD', 'USD', 'BNB', 'PAX', 'TUSD', 'XRP', 'NGN', 'TRX', 'RUB', 'TRY', 'EUR', 'ZAR', 'KRW', 'IDRT', 'BIDR', 'AUD', 'DAI', 'BRL', 'RUB', 'BVND', 'GBP', 'BRL', 'UAH', 'COPS', 'XBT', 'CHF', 'CAD', 'JPY']

    async def fetch_data(self, symbol):
        """Fetch market data for a specific symbol from Kraken asynchronously."""
        if symbol:
            params = {'pair': symbol}  # Kraken uses 'pair' parameter
            async with aiohttp.ClientSession() as session:
                async with session.get(self.api_url, params=params) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        print(f"Error fetching data for {symbol} from Kraken: {response.status}")
                        return None
        return None

    async def fetch_all_data(self):
        """Fetch all market data from Kraken asynchronously."""
        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_url) as response:  # Use the same URL to get all tickers
                if response.status == 200:
                    all_ticker_data = await response.json()
                    if 'result' in all_ticker_data:
                        return all_ticker_data['result']  # Return raw data for normalization
                else:
                    print(f"Error fetching all tickers from Kraken: {response.status}")
                    return None

    def normalize_data(self, ticker_info, symbol):
        """Normalize the fetched data from Kraken."""
        formatted_symbol = self.format_symbol(symbol)
        if ticker_info:
            return {
                'symbol': formatted_symbol,
                'price': float(ticker_info['c'][0]),  # Current price (last trade closed)
                'high': float(ticker_info['h'][0]),    # Today's high price
                'low': float(ticker_info['l'][0]),     # Today's low price
                'volume': float(ticker_info['v'][1]),  # 24h volume
            }
        return None

    def normalize_all_data(self, raw_data):
        """Normalize the fetched data for all tickers from Kraken."""
        normalized_data = []
        for symbol, ticker_info in raw_data.items():
            normalized_entry = self.normalize_data(ticker_info, symbol)
            if normalized_entry:  # Only append if normalization was successful
                normalized_data.append(normalized_entry)
        return normalized_data

    def format_symbol(self, symbol):
        """Format the Kraken symbol as BASE/QUOTE."""
        # Check for known quote currency in the symbol to determine base/quote split
        quote = next((q for q in self.quote_currencies if symbol.endswith(q)), None)
        if quote:
            base = symbol.replace(quote, '')
            return f"{base}/{quote}"
        return symbol  # Return the original symbol if quote currency not found

