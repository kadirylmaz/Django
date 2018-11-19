# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Category(models.Model):
	category_name = models.CharField(max_length=100)
	added_date = models.DateTimeField(auto_now_add=True)
	is_active = models.BooleanField(default=1, blank=False)

	def __str__(self):
		return self.category_name


class BlogPost(models.Model):
	title = models.CharField(max_length=200)
	content = models.CharField(max_length=300)
	added_date = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(null=True, blank=True)
	is_active = models.BooleanField(default=1, blank=False)
	category = models.ForeignKey(
		'Category',
		on_delete=models.CASCADE,
		related_name='category_key'
	)

	def __str__(self):
		return self.title


class Comment(models.Model):
	post = models.ForeignKey(
		'BlogPost',
		on_delete=models.CASCADE,
		related_name='blogpost_key'
	)
	name = models.CharField(max_length=200)
	content = models.TextField(verbose_name='Yorum')
	added_date = models.DateTimeField(auto_now_add=True)
	is_active = models.BooleanField(default=1, blank=False)

	def __str__(self):
		return self.name
