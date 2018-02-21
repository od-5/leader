# coding=utf-8
from annoying.functions import get_object_or_None
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Review

__author__ = 'alexy'


class LandingView(TemplateView):
    template_name = 'landing/index.html'

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)
        context.update({
            'review_list': Review.objects.all()
        })
        return context


class MailView(TemplateView):
    template_name = 'mail.html'

    def get_context_data(self, **kwargs):
        context = super(MailView, self).get_context_data(**kwargs)
        context.update({
            'site_name': settings.SITE_ROOT,
            'name': u'Акакий',
            'id': 1
        })
        return context
