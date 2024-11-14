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

async def test_adapter(adapter_class, symbol_normalization_func):
    """Test a specific adapter with multiple cryptocurrencies."""

    adapter = adapter_class()  # Create an instance of the adapter
    raw_data_list = await adapter.fetch_all_data()

    if raw_data_list is not None:
        normalized_data = adapter.normalize_all_data(raw_data_list['data'] if 'data' in raw_data_list else raw_data_list)
        return normalized_data
        print(f"Number of items fetched from {adapter_class.__name__}: {len(normalized_data)}")
    else:
        print(f"No data fetched from {adapter_class.__name__}.")
    

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


async def main():
    """Run tests for multiple adapters."""
    arbitrage_data_list = []

    # List of adapters and their respective symbol normalization functions
    adapters_info = [
        (BinanceAdapter, lambda s: s.replace('/', '')),   # Test fetch_all_data first
        (CoinbaseAdapter, lambda s: s.replace('/', '-')), # Test fetch_all_data first
        (KrakenAdapter, lambda s: s.replace('/', '')),
        (KuCoinAdapter, lambda s: s.replace('/', '-')),
        (BybitAdapter, lambda s: s.replace('/', '')),    # Add BybitAdapter to the test suite
        (HuobiAdapter, lambda s: s.replace('/', '')),     # Add HuobiAdapter to the test suite
        (BitfinexAdapter, lambda s: 't' + s.replace('/', '')),
        (OKXAdapter, lambda s: 't' + s.replace('/', '')),
    ]

    # Run tests for each adapter
    for adapter_class, symbol_normalization_func in adapters_info:
        result = await test_adapter(adapter_class, symbol_normalization_func)
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
                            f"Profit: {opportunity['profit']}\n")
            
            # Write the formatted string to the file
            file.write(opportunity_str + "\n{'='*50}\n")  # Separate each opportunity with a line of '='

    print("Arbitrage opportunities have been written to finaloutput.txt")


if __name__ == "__main__":
    asyncio.run(main())