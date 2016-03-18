# coding=utf-8
from django.conf.urls import patterns, url
from django.views.generic import TemplateView, DetailView
from apps.blog.models import Post
from .views import PostListView, PostDetailView, PostSectionDetailView
from .ajax import load_more_posts, postcomment_add

__author__ = 'alexy'


urlpatterns = patterns(
    'apps.blog.views',
    url(r'^$', PostListView.as_view(), name='list'),
    # url(r'^post/$', TemplateView.as_view(template_name='blog/post_detail.html'), name='detail'),
    url(r'^(?P<slug>[\w-]+)$', PostDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/txt/$', DetailView.as_view(
        model=Post,
        template_name='blog/post_detail_mail.html'),
        name='detail-txt'
        ),
    url(r'^section/(?P<slug>[\w-]+)$', PostSectionDetailView.as_view(), name='section'),
    url(r'^ajax-load/$', load_more_posts, name='load-more'),
    url(r'^ajax-comment/$', postcomment_add, name='postcomment-add'),
)
