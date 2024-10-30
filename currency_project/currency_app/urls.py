from django.urls import path
from .views import GetCurrentUsd

urlpatterns = [
    path('get-current-usd/', GetCurrentUsd.as_view(), name='get_current_usd'),
]
