'''
@Author: Tye
@Date: 2020-03-23 14:51:44
@LastEditTime: 2020-04-01 20:23:19
@Description: 
'''

from django.conf.urls import url
from django.contrib import admin

from blog.views import (
    IndexView, CategoryView, TagView, SearchView, AuthorView, PostDetailView
)
from config.views import links
from .custom_site import custom_site



urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
    url(r'^author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name='author-list'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post-detail'),
    url(r'^links/$', links, name='links'),
    url(r'^super_admin/', admin.site.urls, name='super-admin'),
    url(r'^admin/', custom_site.urls, name='admin'),  # 配置自定义站点
]
