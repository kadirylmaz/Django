# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Category, BlogPost, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .forms import Category_form, BlogPost_Form

# Create your views here.
args = {}


def admin_home(request):
	return render(request, 'admin_home.html')


def profile_index(request):
	return render(request, 'admin_profile_index.html')


def category_index(request):
	args['category_list'] = category_list = Category.objects.all()
	args['query'] = query = request.GET.get('q')
	if query:
		category_list = category_list.filter(category_name__icontains=query)
	return render(request, 'admin_category_index.html', args)


def category_add(request):
	args['category_list'] = category_list = Category.objects.all()
	if request.POST:
		category_name = request.POST.get('category_name', '')
		is_active = request.POST.get('is_active', 1)

		try:
			new_category = Category.objects.get(id=request.POST.get('category_id'))
		except:
			new_category = None
		if new_category is not None:
			new_category.category_name = category_name
			new_category.is_active = is_active
			new_category.save()
			return render(request, 'sections/category/category_index.html', args)
		else:
			new_category_save_form = Category_form(request.POST)
			if new_category_save_form.is_valid():
				new_category = new_category_save_form.save(commit=False)
				new_category.category_name = category_name
				new_category.is_active = is_active
				new_category.save()
				return render(request, 'sections/category/category_index.html', args)
			else:
				return render(request, 'sections/category/category_index.html', args)


def category_delete(request):
	args['category_list'] = category_list = Category.objects.all()
	if request.POST:
		try:
			category_id = request.POST.get('category_id')
			args['category'] = category = Category.objects.get(id=category_id)
			category.delete()
			return render(request, 'sections/category/category_index.html', args)
		except:
			category = None
			return render(request, 'sections/category/category_index.html', args)
	else:
		pass


def blog_post_index(request):
	args['blog_post_list'] = BlogPost.objects.all()
	args['category_list'] = category_list = Category.objects.all()
	return render(request, 'admin_blog_post_index.html', args)


def comments_index(request):
	args['comments_list'] = Comment.objects.all()
	return render(request, 'admin_comments_index.html', args)


def blog_post_add(request):
	args['blog_post_list'] = BlogPost.objects.all()
	if request.POST:
		title = request.POST.get('title', '')
		content = request.POST.get('content', '')
		category = request.POST.get('category', '')
		is_active = request.POST.get('is_active', 1)

		try:
			current_post = BlogPost.objects.get(id=request.POST.get('blogpost_id'))
		except:
			current_post = None
		if current_post is not None:
			current_post.title = title
			current_post.content = content
			current_post.category_id = category
			current_post.is_active = is_active
			current_post.save()
			return render(request, 'sections/blog_post/blog_post_index.html', args)
		else:
			new_post_form = BlogPost_Form(request.POST)
			if new_post_form.is_valid():
				new_post = new_post_form.save(commit=False)
				new_post.title = title
				new_post.content = content
				new_post.category_id = category
				new_post.is_active = is_active
				new_post.save()
				return render(request, 'sections/blog_post/blog_post_index.html', args)
			else:
				return render(request, 'sections/blog_post/blog_post_index.html', args)
