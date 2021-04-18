from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import AllTransferecesList, CreateTransfer, MyTransferences
from . import views



urlpatterns = [
    path('', login_required(AllTransferecesList.as_view()), 
         name="all_transferences"),
    path('my_transferences/', login_required(MyTransferences.as_view()),
         name="my_transferences"),
    path('create_transfer', login_required(CreateTransfer.as_view()),
         name="create_transfer"),
    path('transactions/', login_required(views.transactions),
         name="transactions"),
    path('succesfull_transfer', login_required(views.succesfull_transfer), 
         name="succesfull_transfer")
]