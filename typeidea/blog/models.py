'''
@Author: Tye
@Date: 2020-03-23 15:55:32
@LastEditTime: 2020-04-14 18:41:27
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \typeidea\typeidea\blog\models.py
'''
from django.db import models
from django.contrib.auth.models import User

import mistune      # 引入markdown三方库

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


    @classmethod
    def get_navs(cls):
        categories = cls.objects.filter(status=cls.STATUS_NORMAL)
        nav_categories = []
        normal_categories = []

        for cate in categories:
            if cate.is_nav:
                nav_categories.append(cate)
            else:
                normal_categories.append(cate)

        return {
            'navs': nav_categories,
            'categories': normal_categories,
        }

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
    content_html = models.TextField(verbose_name="正文html代码", blank=True, editable=False)    # 增加content_html字段用于保存html格式的正文内容
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类")
    tag = models.ManyToManyField(Tag, verbose_name="标签")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    # 新增访问量字段
    pv = models.PositiveIntegerField(default=1)
    uv = models.PositiveIntegerField(default=1)


    # 按照标签id获取文章列表
    @staticmethod
    def get_by_tag(tag_id):
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            tag = None
            post_list = []
        else:
            post_list = tag.post_set.filter(status=Post.STATUS_NORMAL).select_related('owner', 'category')
        
        return post_list, tag

    
    # 按照分类id获取文章列表
    @staticmethod
    def get_by_category(category_id):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            category = None
            post_list = []
        else:
            post_list = category.post_set.filter(status=Post.STATUS_NORMAL).select_related('owner', 'category')
        
        return post_list, category


    # 获取文章列表
    @classmethod
    def latest_posts(cls):
        queryset = cls.objects.filter(status=cls.STATUS_NORMAL)
        return queryset


    # 获取最热门文章列表（按访问量降序排列）
    @classmethod
    def hot_posts(cls):
        return cls.objects.filter(status=cls.STATUS_NORMAL).order_by('-pv').only('title', 'id')


    def __str__(self):
        return self.title

    # 重写save方法，保存content_html
    def save(self, *args, **kwargs):
        self.content_html = mistune.markdown(self.content)
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = verbose_name_plural = "文章"
        ordering = ['-id']  # 根据id进行降序排列
        























