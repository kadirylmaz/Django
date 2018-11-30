from django.conf.urls import url
from .views import *


app_name = 'home'

urlpatterns = [
    url(r'^index/$', home, name='home'),
]
