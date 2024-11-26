from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from libraryApi.accounts.views import RegisterAPIView

urlpatterns = [
    path('login/', ObtainAuthToken.as_view(), name='login'),
    path('register/', RegisterAPIView.as_view(), name='register')
]
