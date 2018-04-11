# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User       # 导入相关的库
import time

class Category(models.Model):                      # ORM中类名对应sql的表名，属性对应的是字段的名字。
    name=models.CharField('名称',max_length=64)
    create_time=models.DateTimeField('添加时间',auto_now_add=True)
    status=models.IntegerField('状态',default=0)

    def __str__(self):              # 当调用这个类时，显示的是对应的name
        return self.name

    class Meta:
        verbose_name='文章分类bbb'
        verbose_name_plural='文章分类bbbbbbb'
        # 使用meta是给这个模型类起一个更可读的名字，在admin管理界面显示的是这里的名字（也就是表头的名字）。一般都是要定义两个属性作为同一个值，plural是verbose_name的复数形式。


def upload_to_goods_img(instance,filename):       # 定义上传文件保存的名字的方法。
    return 'article/{prefix}_{filename}.{suffix}'.format(prefix='article',
                                                filename=int(time.time()*1000),
                                                suffix=filename.split('.')[-1])
# format即格式化文件名，使用 {prefix}_{filename}.{suffix}的形式保存，存放在media文件夹里的article文件夹内。
# filename是用时间模块定义文件名字；
# suffix里的filename是上传的文件的名字，filename.split('.')中，文件扩展名由最后一个 “."决定，如果不含“."则无类型，含有一个或多个“.",由最后一个“."后的字符串决定；无“."则无类型。filename.split('.')[-1]的意思是在以‘.’分隔的文件名中取倒数第一的字母，例如‘jpeg’、‘exe’等文件扩展名。


class Article(models.Model):                                   #  定义一个文章数据表。
    category=models.ForeignKey(Category,verbose_name='分类')   #  定义category为Category的外键，使用Category里的‘分类’列。
    user=models.ForeignKey(User)                               # 定义user为User表的外键。
    title=models.CharField('标题',max_length=128)
    description=models.CharField('描述',max_length=256)
    article=models.TextField('文章')
    create_time=models.DateTimeField('发表时间',auto_now_add=True)
    status=models.IntegerField('状态',default=0)
    img=models.ImageField('图片',upload_to=upload_to_goods_img,null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='文章信息aaa'
        verbose_name_plural='文章信息aaaaaaaa'