from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
args = {}


class LoginForm(forms.Form):
	username = forms.CharField(max_length=100, label='Username')
	password = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput)


class RegisterForm(forms.Form):
	username = forms.CharField(max_length=100, label='Username')
	password = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = [
			'username',
			'password',
		]
