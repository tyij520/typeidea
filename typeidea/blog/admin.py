'''
@Author: Tye
@Date: 2020-03-23 23:56:58
@LastEditTime: 2020-04-03 16:12:36
@LastEditors: Please set LastEditors
@Description: config admin
@FilePath: \typeidea\typeidea\blog\admin.py
'''
from django.contrib import admin
from django.contrib.admin.models import LogEntry    # 引入日志模型类
from django.urls import reverse
from django.utils.html import format_html

from .models import Category, Post, Tag         # 引入模型类
from .adminforms import PostAdminForm           # 引入forms.model类
from typeidea.custom_site import custom_site    # 引入自定义site配置
from typeidea.base_admin import BaseOwnerAdmin  # 引入基类


# Register your models here.
"""分类"""
# 定义关联编辑
class PostInline(admin.TabularInline):  #stackedInline样式不同
    fields = ('title', 'desc')
    extra = 1   # 控制额外多几个
    model = Post


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):    # 此处继承BaseOwnerAdmin基类
    # 配置关联编辑为PostInline
    inlines = [PostInline, ]

    # 配置列表页显示字段
    list_display = ('name', 'status', 'is_nav', 'owner', 'created_time', 'post_count')
    
    # 配置字段
    fields = ('name', 'status', 'is_nav')

    # 配置自定义字段（返回分类下的文章数）
    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = "文章数量"



""" 标签 """
@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'owner','created_time')

    fields = ('name', 'status')



""" 文章 """
# 自定义过滤器
class CategoryOwnerFilter(admin.SimpleListFilter):
    """ 自定义过滤器只展示当前用户分类 """

    title = "分类过滤器"
    parameter_name = "owner_category"

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')
    
    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset



@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    # 配置列表页展示哪些字段
    list_display = ('title', 'category', 'status', 'created_time', 'owner', 'operator')
    
    # 配置哪些字段可以作为链接，点击可以进入编辑页面
    list_display_links = []

    # 配置页面过滤器
    # list_filter = ['category',]
    list_filter = [CategoryOwnerFilter]

    # 配置搜索字段
    search_fields = ['title', 'category__name']

    # 配置动作显示位置
    actions_on_top = True
    actions_on_bottom = True

    # 配置保存、编辑、新建按钮是否在顶部展示
    save_on_top = True

    # 配置form
    form = PostAdminForm

    # 配置数据字段
    exclude = ('owner',)    # 排除的字段

    fieldsets = (
        ("基础配置", {
            'description': "基础配置描述",
            'fields': (
                ('title', 'category'),
                'status',
            ),
        }),
        ("内容", {
            'fields': (
                'desc',
                'content',
            ),
        }),
        ("额外信息", {
            'classes': ('collapse',),
            'fields': ('tag', ),
        }),
    )

    # filter_horizontal = ('tag', )
    filter_vertical = ('tag', )

    # 配置自定义字段
    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = "操作"

    # 添加css、js
    class Meta:
        css = {
            'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css", ),
        }
        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js', )



@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('object_repr', 'object_id', 'action_flag', 'user', 'change_message')