import aiohttp  # Ensure aiohttp is installed
import asyncio

class OKXAdapter:
    def __init__(self):
        self.api_url = 'https://www.okx.com/api/v5/market/tickers?instType=SPOT'  # Directly use the provided URL

    async def fetch_data(self):
        """Fetch market data for a specific symbol from OKX asynchronously."""
        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_url) as response:
                if response.status == 200:
                    data = await response.json()
                    if data.get('data'):
                        return self.normalize_data(data['data'][0])  # Normalize the first ticker data
                else:
                    print(f"Error fetching data from OKX: {response.status}")
                    return None

    async def fetch_all_data(self):
        """Fetch all ticker data from OKX asynchronously."""
        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_url) as response:
                if response.status == 200:
                    data = await response.json()
                    if data.get('data'):
                        self.save_raw_data_to_file(data['data'])  # Save raw data to a text file
                        return data['data']  # Return the raw data without normalization
                else:
                    print(f"Error fetching all ticker data from OKX: {response.status}")
                    return None

    def normalize_data(self, raw_data):
        """Normalize the fetched data for a specific symbol from OKX."""
        if raw_data:
            return {
                'symbol': raw_data['instId'],
                'price': float(raw_data['last']),
                'high': float(raw_data['high24h']),
                'low': float(raw_data['low24h']),
                'volume': float(raw_data['volCcy24h']),
            }
        return None

    def normalize_all_data(self, raw_data_list):
        """Normalize the fetched data for all tickers from OKX and replace '-' with '/'."""
        normalized_data = []
        for raw_data in raw_data_list:
            normalized_entry = {
                'symbol': raw_data['instId'].replace('-', '/'),  # Replace '-' with '/'
                'price': float(raw_data['last']),
                'high': float(raw_data['high24h']),
                'low': float(raw_data['low24h']),
                'volume': float(raw_data['volCcy24h']),
            }
            normalized_data.append(normalized_entry)
        return normalized_data


    def save_raw_data_to_file(self, raw_data):
        """Save raw data to a text file."""
        with open('okx_raw_data.txt', 'w') as f:
            for entry in raw_data:
                f.write(f"{entry}\n")  # Write each entry in a new line
        print("Raw data saved to okx_raw_data.txt")

    async def save_normalized_data_to_file(self, file_path):
        """Fetch, normalize, and save all ticker data to a text file."""
        raw_data = await self.fetch_all_data()
        if raw_data:
            normalized_data = self.normalize_all_data(raw_data)
            with open(file_path, 'w') as file:
                for data in normalized_data:
                    file.write(str(data) + "\n")
            print(f"All normalized data saved to {file_path}")
        else:
            print("No data to save.")

# Example usage:
async def main():
    okx_adapter = OKXAdapter()
    await okx_adapter.save_normalized_data_to_file("okx_normalized_data.txt")

# Run the main function
asyncio.run(main())
