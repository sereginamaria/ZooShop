from web.models import Client
from django import forms


class UserRegister(forms.Form):
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    e_mail = forms.CharField(max_length=50)
    password = forms.PasswordInput()
    repeat_password = forms.PasswordInput()
    phone = forms.CharField(max_length=11)

