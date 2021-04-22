from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views



urlpatterns = [
    path('simple-checkout/', login_required(views.simpleCheckout), name='simple-checkout'),
    path('', login_required(views.store), name='store'),
    path('checkout/<int:pk>/', login_required(views.checkout), name='checkout'),
    path('complete/', login_required(views.paymentComplete), name='complete'),
]