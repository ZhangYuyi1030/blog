# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import IndexView,DetailView_   # 导入views中的2个类

app_name='article'      # 为这个视图起个别名。

urlpatterns=[
    url(r"^index/$", view=IndexView.as_view(), name='index'),      # index的url路由
    url(r"^(?P<pk>\d+)/$", view=DetailView_.as_view(), name='detail'),  # detail的url路由
]