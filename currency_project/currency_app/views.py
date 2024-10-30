import requests
from django.http import JsonResponse
from .models import ExchangeRate
from django.views import View
import time

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"


class GetCurrentUsd(View):
    def get(self, request):
        time.sleep(10)
        response = requests.get(API_URL)
        data = response.json()
        current_rate = data['rates']['RUB']

        ExchangeRate.objects.create(rate=current_rate)

        last_ten_rates = ExchangeRate.objects.order_by('-timestamp')[:10]
        rates_list = [{"rate": rate.rate, "timestamp": rate.timestamp} for rate in last_ten_rates]

        return JsonResponse({
            "current_rate": current_rate,
            "last_rates": rates_list
        })
