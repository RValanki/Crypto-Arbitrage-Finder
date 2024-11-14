import asyncio
import requests
from adapters.binance_adapter import BinanceAdapter
from adapters.coinbase_adapter import CoinbaseAdapter
from adapters.kraken_adapter import KrakenAdapter
from adapters.bitfinex_adapter import BitfinexAdapter
from adapters.kucoin_adapter import KuCoinAdapter
from adapters.bybit_adapter import BybitAdapter
from adapters.huobi_adapter import HuobiAdapter
from adapters.okx_adapter import OKXAdapter

async def fetch_adapter_data(adapter_class):
    """Fetch data for a single adapter and normalize it."""
    adapter = adapter_class()
    try:
        raw_data_list = await adapter.fetch_all_data()
        
        # Check if raw_data_list is a dictionary with a 'data' key, otherwise use it directly if it's a list
        if isinstance(raw_data_list, dict):
            normalized_data = adapter.normalize_all_data(raw_data_list.get('data', raw_data_list))
        elif isinstance(raw_data_list, list):
            normalized_data = adapter.normalize_all_data(raw_data_list)
        else:
            print(f"Unexpected data format from {adapter_class.__name__}.")
            return None

        # Check if normalized_data has been successfully processed
        if normalized_data:
            print(f"Number of items fetched from {adapter_class.__name__}: {len(normalized_data)}")
            return normalized_data
        else:
            print(f"No data fetched from {adapter_class.__name__}.")
            return None
    except Exception as e:
        print(f"Error fetching data from {adapter_class.__name__}: {e}")
        return None


async def test_adapter(adapters_list):
    """Test multiple adapters concurrently."""
    tasks = [fetch_adapter_data(adapter_class) for adapter_class in adapters_list]
    results = await asyncio.gather(*tasks)
    adapters_data = [data for data in results if data is not None]
    return adapters_data

def find_arbitrage_opportunities(normalized_data, exchange_list):
    """Find arbitrage opportunities among the data without duplicates."""
    arbitrage_opportunities = []
    seen_opportunities = set()

    for exchange_index, exchange_data in enumerate(normalized_data):
        for coin1 in exchange_data:
            current_symbol = coin1['symbol']
            min_price = float('inf')
            max_price = 0
            buy_exchange = ""
            sell_exchange = ""

            for comparison_index, exchange_data_comparison in enumerate(normalized_data):
                for coin2 in exchange_data_comparison:
                    if coin2['symbol'] == current_symbol:
                        price = coin2.get('price')
                        if price is None:
                            continue

                        if price < min_price:
                            min_price = price
                            buy_exchange = exchange_list[comparison_index]

                        if price > max_price:
                            max_price = price
                            sell_exchange = exchange_list[comparison_index]

            if max_price > min_price:
                try:
                    profit_percentage = ((max_price - min_price) / min_price) * 100
                    profit = max_price - min_price
                    opportunity_id = (current_symbol, buy_exchange, sell_exchange)

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
                        seen_opportunities.add(opportunity_id)
                except ZeroDivisionError:
                    continue

    arbitrage_opportunities.sort(key=lambda x: x['profitPercentage'], reverse=True)
    return arbitrage_opportunities

async def main():
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

    arbitrage_data_list = await test_adapter(adapters_info)
    print(arbitrage_data_list)
    
    arbitrage_opportunities = find_arbitrage_opportunities(
        arbitrage_data_list,
        ['Binance', 'Coinbase', 'Kraken', 'KuCoin', 'ByBit', 'Huobi', 'Bitfinex', 'OKX']
    )
    print(arbitrage_opportunities)

    with open('finaloutput.txt', 'w') as file:
        for opportunity in arbitrage_opportunities:
            opportunity_str = (f"Symbol: {opportunity['symbol']}\n"
                               f"Buy Exchange: {opportunity['buyExchange']}\n"
                               f"Buy Price: {opportunity['buyPrice']}\n"
                               f"Sell Exchange: {opportunity['sellExchange']}\n"
                               f"Sell Price: {opportunity['sellPrice']}\n"
                               f"Profit Percentage: {opportunity['profitPercentage']:.2f}%\n"
                               f"Profit: {opportunity['profit']}\n")
            file.write(opportunity_str + "\n" + ("=" * 50) + "\n")

    print("Arbitrage opportunities have been written to finaloutput.txt")

if __name__ == "__main__":
    asyncio.run(main())
