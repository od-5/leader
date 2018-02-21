# coding=utf-8
from django.conf.urls import patterns, url

from .views import ticket_send, mail_read

__author__ = 'alexy'


urlpatterns = patterns(
    '',
    url(r'^$', ticket_send, name='send'),
    url(r'^check.png/(?P<pk>\d+)/$', mail_read, name='mail_read'),
)
