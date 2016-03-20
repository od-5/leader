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
    list_display = ('name', 'mail', 'created', 'status', 'comment', 'manager', 'ticket_comment')
    list_filter = ['mail', 'created', 'status', 'manager']
    search_fields = ['mail', 'manager']
    date_hierarchy = 'created'
    fields = ('name', 'phone', 'mail', 'comment', 'status', 'manager', 'ticket_comment')
    form = TicketAdminForm

    def get_queryset(self, request):
        print request.user.is_superuser
        user = request.user
        if user.is_superuser:
            qs = Ticket.objects.all()
        else:
            qs = Ticket.objects.filter(manager=user)
        return qs

admin.site.register(Ticket, TicketAdmin)
