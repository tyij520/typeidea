'''
@Author: Tye
@Date: 2020-03-23 23:56:58
@LastEditTime: 2020-03-26 14:33:11
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \typeidea\typeidea\blog\views.py
'''

from django.shortcuts import render
from django.http import HttpResponse

from .models import Post, Category, Tag
from config.models import SideBar


# Create your views here.
# 列表页展示
def post_list(request, category_id=None, tag_id=None):
    # content = 'post_list category_id={category_id}, tag_id={tag_id}'.format(
    #     category_id=category_id,
    #     tag_id=tag_id,
    # )
    
    # return HttpResponse(content)
    tag = None
    category = None

    if tag_id:
        post_list, tag = Post.get_by_tag(tag_id)
    elif category_id:
        post_list, category = Post.get_by_category(category_id)
    else:
        post_list = Post.latest_posts()
    
    # print(post_list)

    context = {
        'category': category,
        'tag': tag,
        'post_list': post_list,
        'sidebars': SideBar.get_all(),      # 添加侧边栏展示
    }
    context.update(Category.get_navs())     # 添加分类
            
    return render(request, 'blog/list.html', context=context)


# 文章详情页展示
def post_detail(request, post_id):
    # return HttpResponse('detail')
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None
    
    context = {
        'post': post,
        'sidebars': SideBar.get_all(),
    }
    context.update(Category.get_navs())

    return render(request, 'blog/detail.html', context={'post': post})


