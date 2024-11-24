from django.http import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .arbitragedetector import ArbitrageDetector
from .adapters.binance_adapter import BinanceAdapter
from .adapters.coinbase_adapter import CoinbaseAdapter
from .adapters.kraken_adapter import KrakenAdapter
from .adapters.bitfinex_adapter import BitfinexAdapter
from .adapters.kucoin_adapter import KuCoinAdapter
from .adapters.bybit_adapter import BybitAdapter
from .adapters.huobi_adapter import HuobiAdapter
from .adapters.okx_adapter import OKXAdapter

@api_view(['POST'])
def detect_arbitrage(request):
    try:
        # List of adapters for the ArbitrageDetector
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

        # Run the detection
        result = detector.detect_arbitrage()  # Use async if required, adjust accordingly

        # Return the results in the response
        return Response({'success': True, 'data': result}, status=status.HTTP_200_OK)
    except Exception as e:
        # Handle errors gracefully
        return Response({'success': False, 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
