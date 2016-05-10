# -*- coding:utf-8 -*-

from django.db import models
from django.utils import timezone


class Post(models.Model):   # 定义一个Post对象模型
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)  # 定义title为有限制的字符类型
    text = models.TextField()     # 定义text为没有长度限制的长文本，用在blog的内容上
    created_date = models.DateTimeField(blank=True, null=True)    # 定义创建的日期和时间
    published_date = models.DateTimeField(blank=True, null=True)  # 定义发布的日期时间

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
