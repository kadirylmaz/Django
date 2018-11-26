# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import LoginForm, RegisterForm
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


def register_view(request):
	args['form'] = form = RegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username, password=password)
		login(request, new_user)
		return redirect('/')
	return render(request, 'sections/accounts/register.html', args)


def logout_view(request):
	logout(request)
	return redirect('accounts:login')
