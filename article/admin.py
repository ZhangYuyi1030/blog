# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article            # 导入2个数据表。
from .models import Category

admin.site.site_header='''Benny's blog'''    # 设置admin管理页面的窗口标题和页面标题
admin.site.site_title='''Benny's blog'''

class ArticleAdmin(admin.ModelAdmin):                      # 在admin站点管理首页显示文章信息的表头
    list_display = ['title','create_time','description']   # 在文章管理界面显示的字段。
    search_fields = ['title','create_time']                # 搜索框
    actions=None                                           # 进入界面后不采取任何动作。


    def get_queryset(self, request):
        queryset=super(ArticleAdmin,self).get_queryset(request)
        return queryset.filter(status=0)
    # 重写过滤显示，只显示status=0的信息。


    def delete_model(self, request, obj):
        obj.status=1
        obj.save=()
    # 重写admin删除的方法（admin删除时调用的是delete_model）,修改model为逻辑删除（删除后信息仍在数据库，但不会显示出来）。
    # 删除后文章的状态会变为1，显示不出来，修改get_queryset后就能显示出来。

    class Media:
        js=()

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','create_time','status']
    search_fields = ['name','create_time']
    actions=None

    def get_queryset(self, request):
        queryset=super(CategoryAdmin,self).get_queryset(request)
        return queryset.filter(status=0)

    def delete_model(self,request,obj):
        obj.status=1
        obj.save()

admin.site.register(Article,ArticleAdmin)      # 在admin中注册model，也就是把admin和model关联起来。
admin.site.register(Category,CategoryAdmin)