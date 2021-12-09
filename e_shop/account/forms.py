from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from django import forms

from e_shop.settings import AUTH_PASSWORD_VALIDATORS


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput,
                               validators=[validate_password]
                               )
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput,
                                validators=[validate_password]
                                )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
