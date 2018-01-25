# -*- coding: utf-8 -*-
# __author__ = 'apolo'
# _date_ = '2018/1/25 上午10:19'

from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
