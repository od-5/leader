# coding=utf-8
from django.contrib import admin
from suit.admin import SortableModelAdmin
from .models import PostSection, Post, PostComment, BlogSetup

__author__ = 'alexy'


class BlogSetupAdmin(admin.ModelAdmin):
    list_display = ('meta_title', 'meta_key', 'meta_desc')

    def has_add_permission(self, request):
        if self.model.objects.count() != 0:
            return False
        else:
            return True

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
    list_display = ('name', 'created', 'text', 'post', )
    list_filter = ('name', 'mail', 'created', 'post', )


admin.site.register(BlogSetup, BlogSetupAdmin)
admin.site.register(PostSection, PostSectionAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostComment, PostCommentAdmin)
