from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import Index
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('', login_required(Index.as_view()), name="index"),
    
]