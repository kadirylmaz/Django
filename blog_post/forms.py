from django import forms
from .models import Category, BlogPost


class Category_form(forms.ModelForm):
	class Meta:
		model = Category
		exclude = (
			'category_name',
			'added_date',
			'is_active',
		)


class BlogPost_Form(forms.ModelForm):
	class Meta:
		model = BlogPost
		exclude = (
			'title',
			'content',
			'added_date',
			'image',
			'is_active',
			'category',
		)
