# coding=utf-8
from annoying.functions import get_object_or_None
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import PostSection, Post, PostComment, BlogSetup

__author__ = 'alexy'


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        qs = Post.objects.all()[0:3]
        return qs

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data()
        setup = BlogSetup.objects.first()
        context.update({
            'META_TITLE': setup.meta_title,
            'META_KEY': setup.meta_key,
            'META_DESC': setup.meta_desc,
        })
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data()
        if self.object.meta_title:
            meta_title = self.object.meta_title
        else:
            meta_title = self.object.title
        meta_key = self.object.meta_key
        meta_desc = self.object.meta_desc
        context.update({
            'META_TITLE': meta_title,
            'META_KEY': meta_key,
            'META_DESC': meta_desc
        })
        return context


class PostSectionDetailView(DetailView):
    model = PostSection
    template_name = 'blog/post_list.html'

    def get_context_data(self, **kwargs):
        context = super(PostSectionDetailView, self).get_context_data()
        if self.object.meta_title:
            meta_title = self.object.meta_title
        else:
            meta_title = self.object.title
        meta_key = self.object.meta_key
        meta_desc = self.object.meta_desc
        context.update({
            'META_TITLE': meta_title,
            'META_KEY': meta_key,
            'META_DESC': meta_desc
        })
        return context