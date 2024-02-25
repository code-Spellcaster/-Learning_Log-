"""Define el patron de las URL para las cuentas."""

from django.urls import path, include

from . import views

app_name = 'accounts'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # Página de registro.
    path('register/', views.register, name='register'),
]