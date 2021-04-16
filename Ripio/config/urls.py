from django.contrib import admin
from django.urls import path, include
from Users.views import Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('Users.urls')),
    path('accounts/login/', Login.as_view(), name="login"),
    path('contact/', include('Contact.urls')),
    
]
