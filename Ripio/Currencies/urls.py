from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import CurrenciesPriceList , NewCurrency
from .views import ListCurrencies, EditCurrency, DeleteCurrency



urlpatterns = [
    path('currencies_price', 
         login_required(CurrenciesPriceList.as_view()),
         name="currencies_price"),
    path('new_currency', login_required(NewCurrency.as_view()),
         name="new_currency"),
    path('list_currencies', login_required(ListCurrencies.as_view()),
         name="list_currencies"),
    path('edit_currency/<int:pk>/', login_required(EditCurrency.as_view()), 
         name="edit_currency"),
     path('delete_currency/<int:pk>',login_required( DeleteCurrency.as_view()), 
          name='delete_currency'),
     ]