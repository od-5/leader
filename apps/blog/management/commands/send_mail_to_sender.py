# coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail
from apps.sender.models import Sender
from apps.blog.models import Post

__author__ = 'alexy'


class Command(BaseCommand):

    def handle(self, *args, **options):
        sender_qs = Sender.objects.all()
        post_qs = Post.objects.filter(send=False)
        sender_list = [i.mail for i in sender_qs]
        try:
            for post in post_qs:
                # print u'Отправка статьи %s' % post.title
                subject = u'Лидерфраншиз.рф - %s' % post.title
                msg_plain = render_to_string('email.txt', {'object': post})
                msg_html = render_to_string('blog/post_detaila_mail.html', {'object': post})
                send_mail(
                    subject,
                    msg_plain,
                    settings.DEFAULT_FROM_EMAIL,
                    sender_list,
                    html_message=msg_html,
                )
                post.send = True
                post.save()
        except:
            pass
