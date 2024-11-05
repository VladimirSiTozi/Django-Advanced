from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from forumApp.accounts.forms import MyCustomUserForm


class UserRegisterView(CreateView):
    form_class = MyCustomUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')
