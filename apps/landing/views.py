# coding=utf-8
from annoying.functions import get_object_or_None
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

__author__ = 'alexy'