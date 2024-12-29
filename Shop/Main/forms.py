from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль')

    class Meta:
        model = User
        fields = ['username', 'password']


class CreationUserForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        labels = {
            'email': 'Почта',
            'username': 'Логин',
            'password1': 'Пароль',
            'password2': 'Повтор пароля',
        }
        fields = ['username', 'email', 'password1', 'password2']
