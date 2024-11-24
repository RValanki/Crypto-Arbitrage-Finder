from django.urls import path
from . import views

urlpatterns = [
    path('arbitrage/', views.detect_arbitrage, name='detect_arbitrage'),
]
