from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import AccountsBalance, CreateAccount



urlpatterns = [
    path('create_account',
         login_required(CreateAccount.as_view()), 
         name="create_account"),
    path('', login_required(AccountsBalance.as_view()), 
         name="accounts_balance"),
]