from django.conf.urls import url
from django.contrib import admin
from .views import (
    post_home,
    post_list,
    post_create
)

urlpatterns = [
    url(r'^$', post_home, name='post'),
    url(r'^create$', post_create, name='create'),
    url(r'^list$', post_list, name='post'),
    url(r'^$', post_home, name='post'),
    url(r'^$', post_home, name='post'),

]
