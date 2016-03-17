# coding=utf-8
from annoying.functions import get_object_or_None
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import PostSection, Post, PostComment


__author__ = 'alexy'


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        qs = Post.objects.all()[0:3]
        return qs


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostSectionDetailView(DetailView):
    model = PostSection
    template_name = 'blog/post_list.html'
