# coding=utf-8
from django.contrib import admin
from .models import Ticket
from django.forms import ModelForm
from suit.widgets import EnclosedInput, AutosizedTextarea


class TicketAdminForm(ModelForm):
    class Meta:
        widgets = {
            'comment': AutosizedTextarea,
            'ticket_comment': AutosizedTextarea,
        }


class TicketAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created', 'status', 'theme', 'comment')
    list_filter = ['email', 'created', 'status']
    search_fields = ['email', ]
    date_hierarchy = 'created'
    fields = ('name', 'phone', 'email', 'comment', 'status', 'ticket_comment')
    form = TicketAdminForm

admin.site.register(Ticket, TicketAdmin)
