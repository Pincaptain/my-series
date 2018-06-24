from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):

    username = forms.CharField(max_length=255,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'id': 'inputEmail',
                                                             'placeholder': 'Username'}))
    password = forms.CharField(max_length=255,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'id': 'inputPassword',
                                                                 'placeholder': 'Password'}))


class RegisterForm(forms.ModelForm):

    class Meta:

        model = User
        fields = ['email', 'username', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        }
