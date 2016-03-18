# coding=utf-8
from django.conf.urls import patterns, url

__author__ = 'alexy'


urlpatterns = patterns(
    'apps.sender.ajax',
    url(r'^$', 'sender_add', name='add'),
)
