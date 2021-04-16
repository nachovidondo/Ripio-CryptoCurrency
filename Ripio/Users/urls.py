from django.urls import path
from .views import UserRegister, IndexView, Login
urlpatterns = [
    path('register/',UserRegister.as_view(), name="register"),
    path('index/',IndexView.as_view(), name='index'),
    ]
