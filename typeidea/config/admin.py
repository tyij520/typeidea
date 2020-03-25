'''
@Author: Tye
@Date: 2020-03-23 23:56:58
@LastEditTime: 2020-03-25 10:58:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \typeidea\typeidea\config\admin.py
'''
from django.contrib import admin

from .models import Link, SideBar
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin

# Register your models here.
# 友链
@admin.register(Link, site=custom_site)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'created_time')
    
    fields = ('title', 'href', 'status', 'weight')



# 侧边栏
@admin.register(SideBar, site=custom_site)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'display_type', 'content', 'created_time')

    fields = ('title', 'display_type', 'content')