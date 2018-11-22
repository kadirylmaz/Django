"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog_post import views as blog_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', blog_views.admin_home, name="admin_home"),
    url(r'^category/index/$', blog_views.category_index, name="admin_category_index"),
    url(r'^blog-post/index/$', blog_views.blog_post_index, name="admin_blog_post_index"),
    url(r'^comments/index/$', blog_views.comments_index, name="admin_comments_index")
]
