'''
@Author: Tye
@Date: 2020-03-23 23:56:58
@LastEditTime: 2020-04-01 20:24:58
@Description: 
'''

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from django.views.generic import ListView, DetailView   # 导入类视图

from .models import Post, Category, Tag
from config.models import SideBar

from django.db.models import Q      # 用于搜索列表页，优化查询


# Create your views here.
# class-base-view实现方式
# 通用类（分类导航、侧边栏、底部导航）
class CommonViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'sidebars': SideBar.get_all(),
                'keyword': '',  # 此处添加keyword，解决VariableDoesNotExist报错 
            }
        )
        context.update(Category.get_navs())
        return context



# 首页类(展示文章列表)
class IndexView(CommonViewMixin, ListView):     # 继承通用类和ListView
    # 配置查询集
    queryset = Post.latest_posts()
    
    # 配置分页
    paginate_by = 5

    # 指定获取的model列表的变量名，不写的话，默认为object_list 
    context_object_name = "post_list"
    
    # 配置模板名
    template_name = "blog/list.html"



# 分类列表页    (继承首页类)
class CategoryView(IndexView):                  
    def get_context_data(self, **kwargs):
        """ 重写get_context_data方法，添加分类信息"""
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')            # 获取url传递的参数值
        category = get_object_or_404(Category, pk=category_id)  # 判断分类ID是否存在，不存在返回404
        context.update({
            'category': category,
        })
        return context


    def get_queryset(self):
        """ 重写queryset, 根据分类过滤 """
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id)



# 标签列表页    (继承首页类)
class TagView(IndexView):
    def get_context_data(self, **kwargs):
        """ 重写get_context_data方法，添加标签信息"""
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')              # 获取url传递的参数值
        tag = get_object_or_404(Tag, pk=tag_id)         # 判断分类ID1是否存在，不存在返回404
        context.update({
            'tag': tag,
        })
        return context


    def get_queryset(self):
        """ 重写queryset, 根据标签过滤 """
        queryset = super().get_queryset()
        tag_id = self.kwargs.get('tag_id')
        return queryset.filter(tag__id=tag_id)



# 搜索列表页（继承首页类）
class SearchView(IndexView):
    def get_context_data(self):
        """ 添加用户搜索的关键字 """
        context = super().get_context_data()
        context.update({
            'keyword': self.request.GET.get('keyword', '')  # 获取用户提交的keyword，没有就返回空
        })
        return context
    
    
    def get_queryset(self):
        """ 根据关键字过滤 """
        queryset = super().get_queryset()
        keyword = self.request.GET.get('keyword')
        if not keyword:
            return queryset
        return queryset.filter(Q(title__icontains=keyword) | Q(desc__icontains=keyword))






# 作者列表页（继承首页类）
class AuthorView(IndexView):
    def get_queryset(self):
        """ 根据作者id过滤 """
        queryset = super().get_queryset()
        author_id = self.kwargs.get('owner_id')
        return queryset.filter(owner_id=author_id)






# 博文详情页
class PostDetailView(CommonViewMixin, DetailView):
    # 配置查询集
    queryset = Post.latest_posts()

    # 配置模板
    template_name = 'blog/detail.html'

    # 配置变量名
    context_object_name = 'post'

    # 配置查询集过滤条件
    pk_url_kwarg = 'post_id'








# function-view实现方式
# # 列表页展示
# def post_list(request, category_id=None, tag_id=None):
#     tag = None
#     category = None

#     if tag_id:
#         post_list, tag = Post.get_by_tag(tag_id)
#     elif category_id:
#         post_list, category = Post.get_by_category(category_id)
#     else:
#         post_list = Post.latest_posts()
    
#     # print(post_list)

#     context = {
#         'category': category,
#         'tag': tag,
#         'post_list': post_list,
#         'sidebars': SideBar.get_all(),      # 添加侧边栏展示
#     }
#     context.update(Category.get_navs())     # 添加分类
            
#     return render(request, 'blog/list.html', context=context)


# # 文章详情页展示
# def post_detail(request, post_id):
#     # return HttpResponse('detail')
#     try:
#         post = Post.objects.get(id=post_id)
#     except Post.DoesNotExist:
#         post = None
    
#     context = {
#         'post': post,
#         'sidebars': SideBar.get_all(),
#     }
#     context.update(Category.get_navs())

#     return render(request, 'blog/detail.html', context=context)


