# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.utils import timezone
from .models import Post   # .号表示当前目录或当前应用


def post_list(request):
    # posts将视为我们的QuerySet的名字
    # posts从models.py中利用Post类获得值如published_date,author,title
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
