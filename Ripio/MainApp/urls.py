from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import Index



urlpatterns = [
    path('', Index.as_view(), name="index"),
]