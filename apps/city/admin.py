# coding=utf-8
from django.contrib import admin
from .models import City

__author__ = 'alexy'


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'coord_y', 'coord_y')


admin.site.register(City, CityAdmin)
