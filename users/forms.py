from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    # Форма для регистрации нового пользователя
    # Добавление к стандартной форме поля e-mail
    email = forms.EmailField()

    class Meta:
            model = User
            # Вывод нужных полей на форму
            fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    # Форма обнавления пользователя
    email = forms.EmailField()

    class Meta:
        model = User
        # Вывод нужных полей на форму
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    # Форма обнавления профиля
    class Meta:
        # Добавление дополнительных полей
        model = Profile
        fields = ['image']