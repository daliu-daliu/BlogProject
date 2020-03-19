"""
File: urls.py
Author: lvah
Date: 2020-03-17 
Connect: 976131979@qq.com
Description: 

"""

from django.conf.urls import url
from . import views

# /post/1/
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ^: 以什么开头， $是以什么结尾。 [0-9]指单个数字, +代表前面的字符出现1次或者多次。
    # [0-9]+: 1, 2, 2344, 78888,
    # (?P<id>[0-9]+) 关键字匹配
    # /post/1/   ====> 1满足正则规则的， 将id=1
    url(r'^post/(?P<id>[0-9]+)/$', views.detail, name='detail')
]
