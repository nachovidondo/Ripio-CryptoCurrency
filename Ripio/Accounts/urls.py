from django.urls import path
from .views import AccountsBalance
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('', AccountsBalance.as_view(), name="accounts_balance"),
]