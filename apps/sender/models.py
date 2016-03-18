# coding=utf-8
from django.db import models

__author__ = 'alexy'


class Sender(models.Model):
    class Meta:
        verbose_name = u'Подписчик'
        verbose_name_plural = u'Подписчики'
        app_label = 'sender'

    def __unicode__(self):
        return self.email

    mail = models.CharField(max_length=100, verbose_name=u'Адрес электронной почты')
