from django import forms
from django.contrib.auth import authenticate

args = {}


class LoginForm(forms.Form):
	username = forms.CharField(max_length=100, label='Username')
	password = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput)




