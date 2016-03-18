# coding=utf-8
from django.forms import ModelForm
from .models import Sender

__author__ = 'Rylcev Alexy'


class TicketForm(ModelForm):
    class Meta:
        model = Sender
        fields = ('mail', )

