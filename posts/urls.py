from django.conf.urls import url
from django.contrib import admin
from .views import (
    post_create,
    post_detail,
    post_list,
    post_update,
)

urlpatterns = [
    url(r'^create$', post_create, name='create'),
    url(r'^(?P<post_id>\d+)$', post_detail, name='detail'),
    url(r'^list$', post_list, name='list'),
     url(r'^(?P<post_id>\d+)/edit/$', post_update, name='update'),

    # url(r'^$', post_list, name='list'),
    # url(r'^delete$', post_home, name='post'),

]
