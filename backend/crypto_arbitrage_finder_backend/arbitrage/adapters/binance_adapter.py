# File: binance_adapter.py
import ccxt
import asyncio

class BinanceAdapter:
    def __init__(self, symbol=None):
        self.symbol = symbol
        self.exchange = ccxt.binance()

    async def fetch_data(self):
        # Use asyncio.to_thread to run the synchronous fetch_ticker in a thread pool
        if self.symbol:
            return await asyncio.to_thread(self.exchange.fetch_ticker, self.symbol)
        return None

    def normalize_data(self, raw_data):
        if raw_data:
            return {
                'symbol': raw_data['symbol'],
                'price': raw_data['last'],
                'high': raw_data['high'],
                'low': raw_data['low'],
                'volume': raw_data['baseVolume'],
            }
        return None
