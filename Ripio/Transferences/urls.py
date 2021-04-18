from django.urls import path
from .views import AllTransferecesList, CreateTransfer
from . import views



urlpatterns = [
    path('',AllTransferecesList.as_view(), name="all_transferences"),
    path('transactions/', views.transactions, name="transactions"),
    path('create_transfer', CreateTransfer.as_view(), name="create_transfer"),
    path('succesfull_transfer', views.succesfull_transfer, name="succesfull_transfer")
]