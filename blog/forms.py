# -*- coding:utf:8 -*_

# 通过forms，创建一个方式来增加和编辑博客文章

from django import forms    # 导入Django表单
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post     # 使用Post模型创建表单，而Post是我们自定义的
        fields = ('title', 'text',)