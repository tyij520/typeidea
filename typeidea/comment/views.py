'''
@Author: Tye
@Date: 2020-03-23 23:56:58
@LastEditTime: 2020-04-03 14:52:48
@Description: 
'''
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import CommentForm

# Create your views here.
class CommentView(TemplateView):
    http_method_names = ['post']
    template_name = 'comment/result.html'

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        target = request.POST.get('target')

        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.target = target
            instance.save()
            succeed = True
            return redirect(target)
        else:
            succeed = False
        
        context = {
            'succeed': succeed,
            'form': comment_form,
            'target': target,
        }

        return self.render_to_response(context)