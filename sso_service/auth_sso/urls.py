from django.urls import path
from .views import login, TokenVerifyView

urlpatterns = [
    path('api/login/', login, name='login'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token-verify'),
]
