# coding=utf-8
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import LandingView, MailView

__author__ = 'alexy'


urlpatterns = patterns(
    '',
    url(r'^$', LandingView.as_view(), name='index'),
    url(r'^thnx/$', TemplateView.as_view(template_name='landing/ok.html'), name='thnx'),
    url(r'^personal/$', TemplateView.as_view(template_name='landing/personal.html'), name='personal'),
    url(r'^mail/$', MailView.as_view(), name='mail'),
)
