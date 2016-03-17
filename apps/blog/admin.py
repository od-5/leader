# coding=utf-8
from django.contrib import admin
from suit.admin import SortableModelAdmin
from .models import PostSection, Post, PostComment

__author__ = 'alexy'


class PostSectionAdmin(SortableModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    sortable = 'sort'


class PostAdmin(SortableModelAdmin):
    list_display = ('title', 'created', 'preview')
    list_filter = ('created',)
    prepopulated_fields = {'slug': ('title',)}
    sortable = 'sort'

    def preview(self, image):
        try:
            return "<img src='%s' style='width:300px;height:auto;'/>" % image.image.url
        except:
            return None

    preview.short_description = u"Превью"
    preview.allow_tags = True


class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'created', 'text')
    list_filter = ('name', 'mail', 'created')


admin.site.register(PostSection, PostSectionAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostComment, PostCommentAdmin)
