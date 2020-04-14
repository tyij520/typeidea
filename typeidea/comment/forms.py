'''
@Author: Tye
@Date: 2020-04-03 13:41:21
@LastEditTime: 2020-04-03 14:06:23
@Description: comments used Model.Form
'''
from django import forms

from.models import Comment


# 评论需要用到的Form表单模型
class CommentForm(forms.ModelForm):
    # 表单字段-昵称设置
    nickname = forms.CharField(
        label='昵称',
        max_length=50,
        widget=forms.widgets.Input(                  # 控件展示样式
            attrs={'class': 'form-control', 'style': 'width: 60%;'}
        )
    )

    # 表单字段-邮箱设置
    email = forms.CharField(
        label='Email',
        max_length=50,
        widget=forms.widgets.EmailInput(
            attrs={'class': 'form-control', 'style': 'width: 60%;'}
        )
    )

    # 表单字段-网站设置
    website = forms.CharField(
        label='网站',
        max_length=100,
        widget=forms.widgets.URLInput(
            attrs={'class': 'form-control', 'style': 'width: 60%;'}
        )
    )

    # 表单字段-内容设置
    content = forms.CharField(
        label='内容',
        max_length=500,
        widget=forms.widgets.Textarea(
            attrs={'class': 'form-control', 'rows': 6, 'cols': 60}
        )
    )


    # 处理对应宇段数据的方法
    def clean_content(self):
        content = self.cleaned_data.get('content')  # 获取需要处理的字段
        # 判断评论内容，如果内容太少，直接抛出异常
        if len(content) < 10:
            raise forms.ValidationError('内容长度怎么能这么短呢！!')
        return content


    class Meta:
        model = Comment
        fields = ['nickname', 'email', 'website', 'content']


