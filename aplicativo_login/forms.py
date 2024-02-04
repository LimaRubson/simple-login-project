# meu_aplicativo/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import CustomUser

class SignUpForm(UserCreationForm):
    # Adicione campos personalizados se necessário
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

class SignInForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
