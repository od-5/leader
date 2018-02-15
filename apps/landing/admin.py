# coding=utf-8
from django.contrib import admin
from suit.admin import SortableModelAdmin

from .models import Review


class ReviewAdmin(SortableModelAdmin):
    list_display = ('name', 'phone', 'site', 'email', 'city', 'preview')
    sortable = 'sort'

    def preview(self, review):
        try:
            return "<img src='%s' style='width:224px;height:224px;'/>" % review.photo.url
        except:
            return None

    preview.short_description = u"Превью"
    preview.allow_tags = True


admin.site.register(Review, ReviewAdmin)
