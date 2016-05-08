# -*- coding: utf-8 -*-

from django.contrib import admin
# 从models.py中引入对象：Post
from .models import Post

# 为了让模型在admin页面上可见，使用以下命令注册模型
admin.site.register(Post)
