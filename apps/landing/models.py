# coding=utf-8
from PIL import Image
from django.conf import settings
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize
from core.files import upload_to

__author__ = 'alexy'
#
#
# class Setup(models.Model):
#     class Meta:
#         verbose_name = u'Настройки сайта'
#         verbose_name_plural = u'Настройки сайта'
#         app_label = 'landing'
#         ordering = ('id', )
#
#     def __unicode__(self):
#         if self.city:
#             return u'Настройки сайта для города %s' % self.city.name
#         else:
#             return u'Настройки основного сайта'
#
#     def save(self, *args, **kwargs):
#         super(Setup, self).save()
#         if self.logotype:
#             image = Image.open(self.logotype)
#             (width, height) = image.size
#             size = (350, 350)
#             "Max width and height 350"
#             if width > 350:
#                 image.thumbnail(size, Image.ANTIALIAS)
#                 image.save(self.logotype.path, "PNG")
#
#     meta_title = models.TextField(verbose_name=u'Заголовок сайта', blank=True, null=True)
#     meta_keys = models.TextField(verbose_name=u'Ключевые слова', blank=True, null=True)
#     meta_desc = models.TextField(verbose_name=u'Мета описание', blank=True, null=True)
#     email = models.EmailField(verbose_name=u'e-mail для приёма заявок', blank=True)
#     phone = models.CharField(verbose_name=u'Контактный телефон', blank=True, null=True, max_length=20)
#     video_find = models.CharField(verbose_name=u'Видео: как найти наш офис', blank=True, null=True, max_length=256)
#     video = models.TextField(verbose_name=u'HTML-код видео: что получать наши клиенты', blank=True, null=True)
#     top_js = models.TextField(verbose_name=u'Скрипты в <HEAD>..</HEAD>', blank=True)
#     bottom_js = models.TextField(verbose_name=u'Скрипты перед закрывающим </BODY>', blank=True)
#     robots_txt = models.TextField(verbose_name=u'robots.txt', blank=True, null=True)
