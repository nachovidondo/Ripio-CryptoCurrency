from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from Users.views import Login, logoutUsuario



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MainApp.urls')),
    path('users/', include('Users.urls')),
    path('accounts/login/', Login.as_view(), name="login"),
    path('logout/', login_required(logoutUsuario), name="logout"),
    path('contact/', include('Contact.urls')),
    path('accounts/',include('Accounts.urls')),
    path('tranferences/', include('Transferences.urls')),
    path('currencies/', include('Currencies.urls')),
    path('administrator/', include('Administrator.urls')),
    path('API', include('API.urls')),
    ]
