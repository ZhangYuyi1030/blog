# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-04 09:40
from __future__ import unicode_literals

import article.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='\u6807\u9898')),
                ('description', models.CharField(max_length=256, verbose_name='\u63cf\u8ff0')),
                ('article', models.TextField(verbose_name='\u6587\u7ae0')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u8868\u65f6\u95f4')),
                ('status', models.IntegerField(default=0, verbose_name='\u72b6\u6001')),
                ('img', models.ImageField(upload_to=article.models.upload_to_goods_img, verbose_name='\u56fe\u7247')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0\u4fe1\u606f',
                'verbose_name_plural': '\u6587\u7ae0\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='\u540d\u79f0')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('status', models.IntegerField(default=0, verbose_name='\u72b6\u6001')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0\u5206\u7c7b',
                'verbose_name_plural': '\u6587\u7ae0\u5206\u7c7b',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Category', verbose_name='\u5206\u7c7b'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
