'''
@Author: Tye
@Date: 2020-03-25 09:13:26
@LastEditTime: 2020-03-25 09:13:30
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \typeidea\typeidea\blog\adminforms.py
'''
from django import forms


class PostAdminForm(forms.ModelForm):
    # 配置摘要的展示方式
    desc = forms.CharField(widget=forms.Textarea, label="摘要", required=False)

    