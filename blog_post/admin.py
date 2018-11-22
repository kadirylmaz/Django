# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog_post.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(BlogPost)
admin.site.register(Comment)
