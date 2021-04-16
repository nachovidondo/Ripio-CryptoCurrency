from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from Users.views import Login, logoutUsuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('Users.urls')),
    path('accounts/login/', Login.as_view(), name="login"),
    path('logout/', login_required(logoutUsuario), name="logout"),
    path('contact/', login_required(include('Contact.urls'))),
    
]
