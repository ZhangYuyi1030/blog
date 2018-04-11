# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from .models import Article                            # 导入model
from django.views.generic import ListView,DetailView   # 导入django的模块listview和detailview。

class IndexView(ListView):            # 继承listview
    template_name='index.html'        # 指定这个视图的模板为index.html
    model=Article                     # 绑定这个视图对应的model
    ordering=['-create_time']         # 指定文章的排序类型。
    paginate_by = 40l                 # 分页，并指定每页显示的数据。

    def get_queryset(self):             # 过滤已经删除的文章（status不为0的文章）。
        queryset=super(IndexView,self).get_queryset()
        return queryset.filter(status=0)

class DetailView_(DetailView):        # 引入detailview。
    model=Article
    template_name='detail.html'