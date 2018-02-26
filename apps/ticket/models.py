# coding=utf-8
from django.core.mail import send_mail
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from core.phone_inform import getphoneObject
from core.base_model import Common
from core.models import User, Setup
from lib.sms.views import SmsMessage

__author__ = 'alexy'


class Ticket(Common):
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

    manager = models.ForeignKey(to=User, verbose_name=u'Менеджер', blank=True, null=True)
    name = models.CharField(verbose_name=u'Имя', max_length=256)
    phone = models.CharField(verbose_name=u'Телефон', max_length=20)
    mail = models.EmailField(verbose_name=u'e-mail', max_length=100, blank=True, null=True)
    comment = models.TextField(verbose_name=u'Сообщение', blank=True, null=True)
    status = models.PositiveSmallIntegerField(verbose_name=u'Статус заявки', choices=TICKET_STATUS_CHOICE, default=1)
    theme = models.PositiveSmallIntegerField(verbose_name=u'Тема', choices=THEME_CHOICES, default=1)
    ticket_comment = models.TextField(verbose_name=u'Комментарий менеджера', blank=True, null=True)
    sale = models.BooleanField(verbose_name=u'Продажа', default=False)
    price = models.PositiveIntegerField(verbose_name=u'Сумма', blank=True, null=True)
    country = models.CharField(max_length=200, verbose_name=u'Страна', blank=True, null=True)
    city = models.CharField(max_length=200, verbose_name=u'Город', blank=True, null=True)
    time_zone = models.CharField(max_length=10, verbose_name=u'Часовой пояс', blank=True, null=True)
    contact_date = models.DateField(verbose_name=u'Дата контактка', blank=True, null=True)
    mail_view = models.BooleanField(verbose_name=u'Письмо просмотрено', default=False)

    class Meta:
        verbose_name = u'Заявка'
        verbose_name_plural = u'Заявки'
        app_label = 'ticket'

    def __unicode__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     # if not self.country and self.city and self.time_zone:
    #     try:
    #         api_key = settings.HTMLWEB_API_KEY
    #         data = getphoneObject(self.phone, api_key)
    #         try:
    #             self.country = data['fullname']
    #             self.city = data['0']['name']
    #             self.time_zone = data['time_zone']
    #         except:
    #             self.country = data['0']['country']
    #     except:
    #         pass
    #     super(Ticket, self).save(*args, **kwargs)

    def performed_at(self):
        pass

    def send_admin_mail(self):
        setup = Setup.objects.all().first()
        if setup and setup.email:
            email = setup.email
        else:
            email = 'od-5@yandex.ru'
        mail_theme_msg = u'Лидерфраншиз.рф - %s' % self.get_theme_display()
        message = u'Тема: %s\nИмя: %s\nТелефон: %s\nE-mail: %s\nСообщение: %s\n' % \
                  (self.get_theme_display(), self.name, self.phone, self.mail, self.comment)
        send_mail(
            mail_theme_msg,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [email, ]
        )
        return False

    def send_client_mail(self):
        if self.mail:
            subject = u'Материалы по франшизе nadomofone.ru'
            msg_html = render_to_string('mail.html', {'name': self.name, 'id': self.id, 'site_name': settings.SITE_ROOT})
            send_mail(
                subject,
                msg_html,
                settings.DEFAULT_FROM_EMAIL,
                [self.mail, ],
                html_message=msg_html,
            )
        return False


@receiver(post_save, sender=Ticket)
def create_mail(sender, created, **kwargs):
    ticket = kwargs['instance']
    if created:
        ticket.send_admin_mail()
        ticket.send_client_mail()

        message = u'Добрый день! Проверьте вашу почту. Вам высланы материалы по франшизе nadomofone.ru.'
        SmsMessage(ticket.phone, message).send()
