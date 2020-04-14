'''
@Author: Tye
@Date: 2020-03-23 22:56:11
@LastEditTime: 2020-04-03 14:11:49
@LastEditors: Please set LastEditors
@Description: Comment Model
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

    # target = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="评论目标")    
    target = models.CharField(max_length=100, verbose_name="评论目标")  # 修改target字段类型，让其更通用   
    content = models.CharField(max_length=2000, verbose_name="内容")
    nickname = models.CharField(max_length=50, verbose_name="昵称")
    website = models.URLField(verbose_name="网站")
    email = models.EmailField(verbose_name="邮箱")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    # 获取最近评论
    @classmethod
    def latest_comments(cls):
        return cls.objects.filter(status=cls.STATUS_NORMAL).order_by('-created_time')
    

    # 返回指定文章或友链下的所有有效评论
    @classmethod
    def get_by_target(cls, target):
        return cls.objects.filter(target=target, status=cls.STATUS_NORMAL).order_by('-created_time')


    class Meta:
        verbose_name = verbose_name_plural = "评论"
        ordering = ['-id']  # 根据id进行降序排列