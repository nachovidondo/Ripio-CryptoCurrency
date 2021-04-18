from django.urls import path
from .views import CurrenciesPriceList



urlpatterns = [
    path('currencies_price', CurrenciesPriceList.as_view(), name="currencies_price" )

]