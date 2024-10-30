from django.urls import path
from .views import secret_data

urlpatterns = [
    path('secret/', secret_data),
]
