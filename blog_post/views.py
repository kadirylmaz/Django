# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Category,BlogPost,Comment

# Create your views here.
args = {}


def admin_home(request):
	return render(request, 'admin_home.html')


def category_index(request):
	args['category_list'] = Category.objects.all()
	return render(request, 'admin_category_index.html', args)
