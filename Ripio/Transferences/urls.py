from django.urls import path
from .views import TransferecesList



urlpatterns = [
    path('',TransferecesList.as_view(), name="transferences"),
]