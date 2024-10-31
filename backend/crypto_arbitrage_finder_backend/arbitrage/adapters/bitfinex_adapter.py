import aiohttp  # Ensure aiohttp is installed

class BitfinexAdapter:
    def __init__(self):
        self.api_url = 'https://api-pub.bitfinex.com/v2/tickers?symbols=ALL'  # Hardcoded endpoint for all ticker data

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
                            'symbol': entry[0],  # e.g., "tBTCUSD"
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
            normalized_data.append(raw_data)
        
        return normalized_data


