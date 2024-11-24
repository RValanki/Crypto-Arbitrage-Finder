from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from asgiref.sync import async_to_sync
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
    print("Arbitrage detection POST request received")  # Log when the function is called

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

    try:
        print("Calling the detect_arbitrage function asynchronously")  # Log before calling the async function

        # Wrap the async function call with async_to_sync
        sync_detect_arbitrage = async_to_sync(detector.detect_arbitrage)

        # Call the async function without the 'pk' argument, assuming it's not needed
        result = sync_detect_arbitrage()  # No 'pk' argument

        print("Arbitrage detection complete.")  # Log after the detection

        # Return the results in the response
        return Response({'success': True, 'data': result}, status=status.HTTP_200_OK)

    except Exception as e:
        # Log detailed error information
        print(f"Error during arbitrage detection: {str(e)}")  # Log the error
        return Response({'success': False, 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
