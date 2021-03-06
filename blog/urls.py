# -*- coding: utf-8 -*-
"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static

assert isinstance(settings.MEDIA_ROOT, object)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^article/", include('article.urls')),                            # blog的主url配置
    # url(r'$',RedirectView.as_view(url=reverse_lazy('article.index'))),   # 这个不知道是啥。
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)          # 上传文件的路径。
