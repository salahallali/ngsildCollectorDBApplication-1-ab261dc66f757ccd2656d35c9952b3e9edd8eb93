from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    last_name = forms.CharField(label='app name')
    alawed_to_update = forms.BooleanField(required= False, label='allowed to update')
    alawed_to_retrive = forms.BooleanField(label='allowed to retrieve data')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'alawed_to_update', 'alawed_to_retrive']
