'''
@Author: Tye
@Date: 2020-03-23 23:56:58
@LastEditTime: 2020-03-25 10:56:18
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \typeidea\typeidea\comment\admin.py
'''
from django.contrib import admin

from .models import Comment
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin

# Register your models here.
""" 评论 """
@admin.register(Comment, site=custom_site)
class CommentAdmin(BaseOwnerAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')