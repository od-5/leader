# coding=utf-8
from annoying.decorators import ajax_request
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from .forms import SenderForm

__author__ = 'alexy'


@ajax_request
def sender_add(request):
    if request.method == "POST":
        form = SenderForm(data=request.POST)
        if form.is_valid():
            form.save()
            return {
                'sender': True
            }
        return {
            'error': True
        }
    return {
        'error': True
    }
