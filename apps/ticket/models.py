# coding=utf-8
from django.db import models
from core.base_model import Common

__author__ = 'alexy'


class Ticket(Common):
    class Meta:
        verbose_name = u'Заявка'
        verbose_name_plural = u'Заявки'
        app_label = 'ticket'

    def __unicode__(self):
        return self.name

    def performed_at(self):
        pass

    TICKET_STATUS_CHOICE = (
        (0, u'В обработке'),
        (1, u'Новая заявка'),
        (2, u'Отклонена'),
        (3, u'Нет ответа'),
    )

    THEME_CHOICES = (
        (1, u'Получить информацию об условиях открытия бизнеса'),
        (2, u'Получить подробную консультацию о франшизе'),
        (3, u'Получить презентацию с перечнем свободных городов'),
    )

    name = models.CharField(verbose_name=u'Имя', max_length=256)
    phone = models.CharField(verbose_name=u'E-mail', max_length=20)
    email = models.EmailField(verbose_name=u'e-mail', max_length=100, blank=True, null=True)
    comment = models.TextField(verbose_name=u'Сообщение', blank=True, null=True)
    status = models.PositiveSmallIntegerField(verbose_name=u'Статус заявки',  choices=TICKET_STATUS_CHOICE, default=1)
    theme = models.PositiveSmallIntegerField(verbose_name=u'Тема',  choices=THEME_CHOICES, default=1)
    ticket_comment = models.TextField(verbose_name=u'Комментарий', blank=True, null=True)
