from django.urls import path
from toDoApp.accounts.views import RegisterView, LoginView, LogoutApiView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutApiView.as_view(), name='logout')
]