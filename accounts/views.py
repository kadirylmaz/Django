# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
args = {}


def login_view(request):
	args['form'] = form = LoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect('/')
	return render(request, 'sections/accounts/login.html', args)


def logout_view(request):
	logout(request)
	return redirect('accounts:login')
