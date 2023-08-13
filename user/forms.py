from typing import Any
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')
        if len(email) > 100:
            raise forms.ValidationError('Email is too long')
        return email
    

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'form-control'}),
        }
    
