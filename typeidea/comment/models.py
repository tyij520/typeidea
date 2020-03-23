'''
@Author: Tye
@Date: 2020-03-23 22:56:11
@LastEditTime: 2020-03-23 23:24:47
@LastEditors: Please set LastEditors
@Description: Comment Model
@FilePath: \typeidea\typeidea\comment\models.py
'''
from django.db import models

from blog.models import Post    # 导入Post类，用于设置外键关联

# Create your models here.
# """ 评论模型 """
class Comment(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, "正常"),
        (STATUS_DELETE, "删除"),
    )

    target = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="评论目标")
    content = models.CharField(max_length=2000, verbose_name="内容")
    nickname = models.CharField(max_length=50, verbose_name="昵称")
    website = models.URLField(verbose_name="网站")
    email = models.EmailField(verbose_name="邮箱")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "评论"
