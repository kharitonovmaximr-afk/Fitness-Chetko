from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class CustomRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Введите пароль',
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Повторите пароль',
        })
    )
    class Meta:
        model = CustomUser
        fields = ['username', 'last_name', 'email', 'password1', 'password2', 'age', 'health_group']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Введите имя',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'example@yandex.ru'
            }),
            'age': forms.NumberInput(attrs={
                'placeholder': '18'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Введите фамилию',
            }),
        }


class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(max_length=96, widget=forms.EmailInput(attrs={
        'autofocus':True,
        'autocomplate':'email',
        'placeholder': 'example@yandex.ru'
    }))
    password = forms.CharField(max_length=96, widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль'
    }))
