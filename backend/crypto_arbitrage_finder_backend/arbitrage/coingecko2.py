import os
import base64
import aiohttp
from bs4 import BeautifulSoup
import asyncio
from arbitragedetector import ArbitrageDetector
from adapters.binance_adapter import BinanceAdapter
from adapters.coinbase_adapter import CoinbaseAdapter
from adapters.kraken_adapter import KrakenAdapter
from adapters.bitfinex_adapter import BitfinexAdapter
from adapters.kucoin_adapter import KuCoinAdapter
from adapters.bybit_adapter import BybitAdapter
from adapters.huobi_adapter import HuobiAdapter
from adapters.okx_adapter import OKXAdapter


def sanitize_filename(symbol):
    """
    Replace invalid characters in the symbol to create a valid filename.
    """
    return symbol.replace("/", "_").replace("\\", "_").replace(" ", "_")


async def fetch_image_data(session, query):
    """
    Fetch the first relevant image from a search query and return the image data as Base64.
    """
    try:
        search_url = f"https://www.google.com/search?hl=en&tbm=isch&q={query}"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

        async with session.get(search_url, headers=headers) as response:
            if response.status == 200:
                html_content = await response.text()
                soup = BeautifulSoup(html_content, 'html.parser')
                image_tags = soup.find_all('img')

                if len(image_tags) > 1:  # Skip the first image tag if it's not relevant
                    first_image_url = image_tags[1]['src']

                    # Fetch the image data
                    async with session.get(first_image_url) as img_response:
                        if img_response.status == 200:
                            image_data = await img_response.read()
                            return base64.b64encode(image_data).decode('utf-8')
                        else:
                            print(f"Failed to fetch image from {first_image_url}, Status code: {img_response.status}")
                            return None
                else:
                    print(f"No suitable image found for query: {query}")
                    return None
            else:
                print(f"Failed to fetch search results for query: {query}, Status code: {response.status}")
                return None
    except Exception as e:
        print(f"Error fetching image for query: {query}, Error: {e}")
        return None


async def main():
    """
    Main function to detect arbitrage opportunities and fetch images for the associated symbols.
    """
    # List of exchange adapters
    adapters_info = [
        BinanceAdapter,
        CoinbaseAdapter,
        KrakenAdapter,
        KuCoinAdapter,
        BybitAdapter,
        HuobiAdapter,
        BitfinexAdapter,
        OKXAdapter,
    ]

    # Initialize the ArbitrageDetector
    detector = ArbitrageDetector(adapters_info)

    # Detect arbitrage opportunities
    print("Detecting arbitrage opportunities...")
    result = await detector.detect_arbitrage()

    # Fetch images for each arbitrage opportunity
    print("Fetching images for detected arbitrage opportunities...")
    async with aiohttp.ClientSession() as session:
        tasks = []
        for arb in result:
            symbol = arb['symbol']
            sanitized_symbol = sanitize_filename(symbol)  # Sanitize the symbol
            query = f"{symbol} logo crypto"
            tasks.append(fetch_image_data(session, query))

        images = await asyncio.gather(*tasks)

    # Add the image data as a new field in the result array
    for i, arb in enumerate(result):
        arb['icon'] = images[i] if images[i] else None

    print("Arbitrage opportunities with icons:", result)


if __name__ == "__main__":
    asyncio.run(main())
