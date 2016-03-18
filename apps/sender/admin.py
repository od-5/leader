# coding=utf-8
from django.contrib import admin
from .models import Sender

__author__ = 'alexy'


class SenderAdmin(admin.ModelAdmin):
    list_display = ('mail', )


admin.site.register(Sender, SenderAdmin)
