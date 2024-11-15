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

class ArbitrageDetector:
    def __init__(self, adapters_info):
        self.adapters_info = adapters_info
        self.exchange_names = []
        self.getExchangeNames()

    def getExchangeNames(self):
        for adapter in self.adapters_info:
            self.exchange_names.append(adapter().exchangeName)
    
    async def fetch_adapter_data(self, adapter_class):
        """Fetch data for a single adapter and normalize it."""
        adapter = adapter_class()
        try:
            raw_data_list = await adapter.fetch_all_data()
            
            if isinstance(raw_data_list, dict):
                normalized_data = adapter.normalize_all_data(raw_data_list.get('data', raw_data_list))
            elif isinstance(raw_data_list, list):
                normalized_data = adapter.normalize_all_data(raw_data_list)
            else:
                print(f"Unexpected data format from {adapter_class.__name__}.")
                return None

            if normalized_data:
                print(f"Number of items fetched from {adapter_class.__name__}: {len(normalized_data)}")
                return normalized_data
            else:
                print(f"No data fetched from {adapter_class.__name__}.")
                return None
        except Exception as e:
            print(f"Error fetching data from {adapter_class.__name__}: {e}")
            return None

    async def fetch_all_data(self):
        """Test multiple adapters concurrently."""
        tasks = [self.fetch_adapter_data(adapter_class) for adapter_class in self.adapters_info]
        results = await asyncio.gather(*tasks)
        adapters_data = [data for data in results if data is not None]
        return adapters_data

    def find_arbitrage_opportunities(self, normalized_data):
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
                buy_volume = buy_high = buy_low = None
                sell_volume = sell_high = sell_low = None
                buy_fee = sell_fee = 0

                for comparison_index, exchange_data_comparison in enumerate(normalized_data):
                    for coin2 in exchange_data_comparison:
                        if coin2['symbol'] == current_symbol:
                            price = coin2.get('price')
                            volume = coin2.get('volume')
                            high = coin2.get('high')
                            low = coin2.get('low')
                            if price is None:
                                continue

                            # Adjust the price based on fees
                            if price < min_price:
                                min_price = price
                                buy_exchange = self.exchange_names[comparison_index]
                                buy_volume = volume
                                buy_high = high
                                buy_low = low
                                buy_fee = self.adapters_info[comparison_index]().takerFee

                            if price > max_price:
                                max_price = price
                                sell_exchange = self.exchange_names[comparison_index]
                                sell_volume = volume
                                sell_high = high
                                sell_low = low
                                sell_fee = self.adapters_info[comparison_index]().takerFee

                if max_price > min_price:
                    try:
                        # Calculate profit before fees
                        profit = max_price - min_price

                        # Apply fees for both buy and sell
                        profit_after_fees = profit - (min_price * buy_fee) - (max_price * sell_fee)

                        # Calculate profit percentage before fees
                        profit_percentage = (profit / min_price) * 100

                        # Calculate profit percentage after fees
                        profit_percentage_after_fees = ((profit_after_fees) / min_price) * 100

                        opportunity_id = (current_symbol, buy_exchange, sell_exchange)

                        # Only add the opportunity if profitPercentageAfterFees <= 200
                        if profit_percentage_after_fees <= 200 and opportunity_id not in seen_opportunities:
                            arbitrage_opportunities.append({
                                'symbol': current_symbol,
                                'buyExchange': buy_exchange,
                                'buyPrice': min_price,
                                'buyVolume': buy_volume,
                                'buyHigh': buy_high,
                                'buyLow': buy_low,
                                'sellExchange': sell_exchange,
                                'sellPrice': max_price,
                                'sellVolume': sell_volume,
                                'sellHigh': sell_high,
                                'sellLow': sell_low,
                                'profit': profit,
                                'profitPercentage': profit_percentage,  # Keep the original profit percentage
                                'profitAfterFees': profit_after_fees,
                                'profitPercentageAfterFees': profit_percentage_after_fees
                            })
                            seen_opportunities.add(opportunity_id)
                    except ZeroDivisionError:
                        continue

        arbitrage_opportunities.sort(key=lambda x: x['profitPercentageAfterFees'], reverse=True)
        return arbitrage_opportunities




    async def detect_arbitrage(self):
        """Detect arbitrage opportunities and save to a file."""
        # Fetch data from adapters
        arbitrage_data_list = await self.fetch_all_data()
        
        # Find arbitrage opportunities
        arbitrage_opportunities = self.find_arbitrage_opportunities(arbitrage_data_list)

        # Write arbitrage opportunities to a file
        with open('finaloutput.txt', 'w') as file:
            for opportunity in arbitrage_opportunities:
                opportunity_str = (f"Symbol: {opportunity['symbol']}\n"
                               f"Buy Exchange: {opportunity['buyExchange']}\n"
                               f"Buy Price: {opportunity['buyPrice']}\n"
                               f"Buy Volume: {opportunity['buyVolume']}\n"
                               f"Buy High: {opportunity['buyHigh']}\n"
                               f"Buy Low: {opportunity['buyLow']}\n"
                               f"Sell Exchange: {opportunity['sellExchange']}\n"
                               f"Sell Price: {opportunity['sellPrice']}\n"
                               f"Sell Volume: {opportunity['sellVolume']}\n"
                               f"Sell High: {opportunity['sellHigh']}\n"
                               f"Sell Low: {opportunity['sellLow']}\n"
                               f"Profit: {opportunity['profit']}\n"
                               f"Profit Percentage: {opportunity['profitPercentage']:.2f}%\n"
                               f"Profit After Fees: {opportunity['profitAfterFees']}\n"
                               f"Profit Percentage After Fees: {opportunity['profitPercentageAfterFees']:.2f}%")
                file.write(opportunity_str + "\n" + ("=" * 50) + "\n")

        print("Arbitrage opportunities have been written to finaloutput.txt")
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

    
    detector = ArbitrageDetector(adapters_info)
    result = await detector.detect_arbitrage()
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
