import asyncio
import requests
from adapters.binance_adapter import BinanceAdapter  # Adjust the import according to your project structure
from adapters.coinbase_adapter import CoinbaseAdapter
from adapters.kraken_adapter import KrakenAdapter
from adapters.bitfinex_adapter import BitfinexAdapter
from adapters.kucoin_adapter import KuCoinAdapter
from adapters.bybit_adapter import BybitAdapter  # Import the Bybit adapter
from adapters.huobi_adapter import HuobiAdapter  # Import the Huobi adapter
from adapters.okx_adapter import OKXAdapter

def fetch_top_cryptos():
    """Fetch the top cryptocurrencies from CoinGecko."""
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 200,
        'page': 1,
        'sparkline': False,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return [coin['symbol'].upper() + '/USDT' for coin in response.json()]
    else:
        print(f"Error fetching top cryptocurrencies: {response.status_code}, Message: {response.text}")
        return []

async def fetch_and_normalize_data(adapter):
    """Fetch and normalize data from a given adapter."""
    try:
        raw_data = await adapter.fetch_data()  # Fetch raw data asynchronously
        if raw_data:
            return adapter.normalize_data(raw_data)
        else:
            print(f"No data returned for {adapter.symbol}.")
            return None
    except Exception as e:
        print(f"Error fetching data for {adapter.symbol}: {e}")
        return None  # Return None on error

async def test_adapter(adapter_class, top_symbols, symbol_normalization_func, fetch_all=False):
    """Test a specific adapter with multiple cryptocurrencies."""
    print(f"Testing {'fetch_all_data' if fetch_all else 'individual fetch'} method for {adapter_class.__name__}...")

    adapter = adapter_class()  # Create an instance of the adapter

    if fetch_all:
        raw_data_list = await adapter.fetch_all_data()
        if raw_data_list is not None:
            normalized_data = adapter.normalize_all_data(raw_data_list['data'] if 'data' in raw_data_list else raw_data_list)
            return normalized_data
            #print(normalized_data)
            print(f"Number of items fetched from {adapter_class.__name__}: {len(normalized_data)}")
        else:
            print(f"No data fetched from {adapter_class.__name__}.")
    else:
        normalized_symbols = [symbol_normalization_func(symbol) for symbol in top_symbols]
        tasks = [fetch_and_normalize_data(adapter_class(symbol)) for symbol in normalized_symbols]
        normalized_data_list = await asyncio.gather(*tasks)

        successful_fetches = sum(1 for data in normalized_data_list if data is not None)

        print(f"Number of successful fetches: {successful_fetches}")
        for normalized_data in normalized_data_list:
            if normalized_data:
                print(f"{adapter_class.__name__} Normalized Data:", normalized_data)

def find_arbitrage_opportunities(normalized_data, exchange_list):
    """Find arbitrage opportunities among the data without duplicates."""
    arbitrage_opportunities = []
    seen_opportunities = set()  # To keep track of unique opportunities

    # Iterate through each exchange's data in normalized_data
    for exchange_index, exchange_data in enumerate(normalized_data):
        for coin1 in exchange_data:
            current_symbol = coin1['symbol']

            # Initialize variables for the lowest and highest prices
            min_price = float('inf')
            max_price = 0
            buy_exchange = ""
            sell_exchange = ""

            # Compare the current coin against all other exchanges
            for comparison_index, exchange_data_comparison in enumerate(normalized_data):
                for coin2 in exchange_data_comparison:
                    if coin2['symbol'] == current_symbol:
                        price = coin2.get('price')

                        if price is None:
                            continue  # Skip if price is not available

                        # Find the lowest price for buying
                        if price < min_price:
                            min_price = price
                            buy_exchange = exchange_list[comparison_index]

                        # Find the highest price for selling
                        if price > max_price:
                            max_price = price
                            sell_exchange = exchange_list[comparison_index]

            # Check if there is an arbitrage opportunity (selling price > buying price)
            if max_price > min_price:
                try:
                    profit_percentage = ((max_price - min_price) / min_price) * 100
                    profit = max_price - min_price

                    # Create a unique identifier for the opportunity
                    opportunity_id = (current_symbol, buy_exchange, sell_exchange)

                    # Check if this opportunity has been seen before
                    if opportunity_id not in seen_opportunities:
                        arbitrage_opportunities.append({
                            'symbol': current_symbol,
                            'buyExchange': buy_exchange,
                            'buyPrice': min_price,
                            'sellExchange': sell_exchange,
                            'sellPrice': max_price,
                            'profitPercentage': profit_percentage,
                            'profit': profit
                        })
                        # Add to the set of seen opportunities
                        seen_opportunities.add(opportunity_id)
                except ZeroDivisionError:
                    # If ZeroDivisionError occurs, skip this iteration
                    continue

    # Sort arbitrage opportunities by profit percentage in descending order
    arbitrage_opportunities.sort(key=lambda x: x['profitPercentage'], reverse=True)
    return arbitrage_opportunities






def write_arbitrage_data_to_file(arbitrage_data_list):
    print(arbitrage_data_list)
    """Write arbitrage data to a file."""
    with open('allarbitragedata.txt', 'w') as file:
        for adapter_list in arbitrage_data_list:
            for data in adapter_list:
                # Writing in the format {'symbol': 'STX/USDT', 'price': 1.9105, 'high': 2.0806, 'low': 1.8185, 'volume': 14067687.93364553}
                file.write(f"{{'symbol': '{data['symbol']}', 'price': {data['price']}, 'high': {data['high']}, 'low': {data['low']}, 'volume': {data['volume']}}}\n")
    print(f"Arbitrage data written to allarbitragedata.txt")


async def main():
    """Run tests for multiple adapters."""
    arbitrage_data_list = []
    print("Fetching top cryptocurrencies...")
    top_symbols = fetch_top_cryptos()  # Fetch top cryptocurrencies once

    # List of adapters and their respective symbol normalization functions
    adapters_info = [
        (BinanceAdapter, lambda s: s.replace('/', ''), True),   # Test fetch_all_data first
        (CoinbaseAdapter, lambda s: s.replace('/', '-'), True), # Test fetch_all_data first
        (KrakenAdapter, lambda s: s.replace('/', ''), True),
        (KuCoinAdapter, lambda s: s.replace('/', '-'), True),
        (BybitAdapter, lambda s: s.replace('/', ''), True),    # Add BybitAdapter to the test suite
        (HuobiAdapter, lambda s: s.replace('/', ''), True),     # Add HuobiAdapter to the test suite
        (BitfinexAdapter, lambda s: 't' + s.replace('/', ''), True),
        (OKXAdapter, lambda s: 't' + s.replace('/', ''), True),
    ]

    # Run tests for each adapter
    for adapter_class, symbol_normalization_func, fetch_all in adapters_info:
        result = await test_adapter(adapter_class, top_symbols, symbol_normalization_func, fetch_all)
        print(result)
        print("mao")
        arbitrage_data_list.append(result)
        # Adding a delay to prevent rate limiting
        await asyncio.sleep(1)
    
    # Example code to write the arbitrage opportunities to a file
    arbitrage_opportunities = find_arbitrage_opportunities(arbitrage_data_list, ['Binance', 'Coinbase', 'Kraken', 'KuCoin', 'ByBit', 'Huobi', 'Bitfinex', 'OKX'])
    print(arbitrage_opportunities)
    # Open the file in write mode
    with open('finaloutput.txt', 'w') as file:
        # Iterate over the arbitrage opportunities and write them into the file
        for opportunity in arbitrage_opportunities:
            # Create a formatted string for each arbitrage opportunity
            opportunity_str = (f"Symbol: {opportunity['symbol']}\n"
                            f"Buy Exchange: {opportunity['buyExchange']}\n"
                            f"Buy Price: {opportunity['buyPrice']}\n"
                            f"Sell Exchange: {opportunity['sellExchange']}\n"
                            f"Sell Price: {opportunity['sellPrice']}\n"
                            f"Profit Percentage: {opportunity['profitPercentage']:.2f}%\n"
                            f"Profit: {opportunity['profit']:.2f}\n")
            
            # Write the formatted string to the file
            file.write(opportunity_str + "\n{'='*50}\n")  # Separate each opportunity with a line of '='

    print("Arbitrage opportunities have been written to finaloutput.txt")


if __name__ == "__main__":
    asyncio.run(main())
