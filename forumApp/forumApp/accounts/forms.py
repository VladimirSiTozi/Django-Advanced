from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class MyCustomUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()  # it knows for our custom model, because of settings AUTH_USER_MODEL config
        fields = ('username', 'email',)


