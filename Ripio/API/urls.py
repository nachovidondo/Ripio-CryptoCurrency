from django.urls import path
from API.views.transfer_views import TransferList
from API.views.currency_views import CurrencyList
from API.views.accounts_views import AccountList
from API.views.accounts_views import AccountRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('transfer/',TransferList.as_view(), name="transfer"),
    path('currency/',CurrencyList.as_view(), name='currency'),
    path('accounts/', AccountList.as_view(), name='accounts'),
    path('account_retrieve_update_destroy/<int:pk>/'
         ,AccountRetrieveUpdateDestroyAPIView.as_view(),
         name="account_retrieve_update_destroy"),
    
    
]
