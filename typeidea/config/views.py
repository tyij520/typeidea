'''
@Author: Tye
@Date: 2020-03-23 23:56:58
@LastEditTime: 2020-04-02 14:21:13
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''

from django.shortcuts import render
from django.http import HttpResponse

# 引入公共视图类
from django.views.generic import ListView
from blog.views import CommonViewMixin      

from .models import Link



# Create your views here.
class LinkListView(CommonViewMixin, ListView):
    queryset = Link.objects.filter(status=Link.STATUS_NORMAL)
    template_name = 'config/links.html'
    context_object_name = 'link_list'
