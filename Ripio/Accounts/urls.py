from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import AccountsBalance



urlpatterns = [
    path('', login_required(AccountsBalance.as_view()), name="accounts_balance"),
]