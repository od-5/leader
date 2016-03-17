# coding=utf-8
from annoying.decorators import ajax_request
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from core.models import Setup
from .forms import TicketForm

__author__ = 'alexy'


@ajax_request
@csrf_exempt
def ticket(request):
    # try:
    #     email = Setup.objects.all()[0].email
    # except:
    #     email = 'od-5@yandex.ru'
    email = 'od-5@yandex.ru'
    if request.method == "POST":
        form = TicketForm(data=request.POST)
        theme = request.POST.get('theme')
        print theme
        if form.is_valid():
            print form
            ticket = form.save(commit=False)
            ticket.status = 1
            ticket.theme = int(theme)
            ticket.save()
            mail_theme_msg = u'Лидерфраншиз.рф - %s' % ticket.get_theme_display()
            if ticket.comment:
                message = u'Тема: %s\nИмя: %s\nТелефон: %s\nE-mail: %s\nСообщение: %s\n' % \
                          (ticket.get_theme_display(), ticket.name, ticket.phone, ticket.email, ticket.comment)
            else:
                message = u'Тема: %s\nИмя: %s\nТелефон: %s\nE-mail: %s\n' % \
                          (ticket.get_theme_display(), ticket.name, ticket.phone, ticket.email)
            send_mail(
                mail_theme_msg,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [email, ]
            )
            return {
                'success': 'Message send'
            }

    return {
        'success': True
    }
