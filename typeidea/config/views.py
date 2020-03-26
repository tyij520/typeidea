'''
@Author: Tye
@Date: 2020-03-23 23:56:58
@LastEditTime: 2020-03-25 14:48:23
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \typeidea\typeidea\config\views.py
'''

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def links(request):
    return HttpResponse('links')
