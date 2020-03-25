'''
@Author: Tye
@Date: 2020-03-23 15:55:32
@LastEditTime: 2020-03-24 21:39:16
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \typeidea\typeidea\blog\models.py
'''
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# """ 分类模型"""
class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    name = models.CharField(max_length=50, verbose_name="名称")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    is_nav= models.BooleanField(default=False, verbose_name="是否为导航")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "分类"



# """ 标签模型 """
class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    
    name = models.CharField(max_length=10, verbose_name="名称")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "标签"



# """ 文章模型 """
class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0   
    STATUS_DRAFT = 2    # 草稿状态
    STATUS_ITEMS = (
        (STATUS_NORMAL, "正常"),
        (STATUS_DELETE, "删除"),
        (STATUS_DRAFT, "草稿"),
    )

    title = models.CharField(max_length=255, verbose_name="标题")
    desc =models.CharField(max_length=1024, blank=True, verbose_name="摘要")
    content = models.TextField(verbose_name="正文", help_text="正文必须为MarkDown格式！")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类")
    tag = models.ManyToManyField(Tag, verbose_name="标签")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "文章"
        ordering = ['-id']  # 根据id进行降序排列
        























