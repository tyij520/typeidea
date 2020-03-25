'''
@Author: Tye
@Date: 2020-03-25 09:41:36
@LastEditTime: 2020-03-25 09:48:55
@LastEditors: Please set LastEditors
@Description: custom site
@FilePath: \typeidea\typeidea\typeidea\custom_site.py
'''

from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = "Typeidea"
    site_title = "Typeidea管理后台"
    index_title = "首页"


custom_site = CustomSite(name='cus_admin')
