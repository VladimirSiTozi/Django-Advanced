from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class MyCustomUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()  # it knows for our custom model, because of settings AUTH_USER_MODEL config
        fields = ('username', 'email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = '__all__'
