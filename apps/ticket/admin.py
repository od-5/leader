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
    list_display = ('name', 'phone', 'mail', 'created', 'status', 'manager', 'country', 'city', 'time_zone')
    list_filter = ['mail', 'created', 'status', 'manager', 'contact_date']
    search_fields = ['mail', 'manager']
    date_hierarchy = 'created'
    readonly_fields = ('country', 'city', 'time_zone')
    fields = ('name', 'phone', 'mail', 'comment', 'country', 'city', 'time_zone', 'status', 'contact_date', 'manager', 'ticket_comment', 'sale')
    form = TicketAdminForm

    def get_queryset(self, request):
        print request.user.is_superuser
        user = request.user
        if user.is_superuser:
            qs = Ticket.objects.filter(sale=False)
        else:
            qs = Ticket.objects.filter(manager=user, sale=False)
        return qs


class Sale(Ticket):
    class Meta:
        proxy = True
        verbose_name = u'Продажа'
        verbose_name_plural = u'Продажи'


class SaleAdminForm(ModelForm):
    class Meta:
        widgets = {
            'price': EnclosedInput(append=u'руб.'),
            'comment': AutosizedTextarea,
            'ticket_comment': AutosizedTextarea,
        }


class SaleAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        user = request.user
        if user.is_superuser:
            return self.model.objects.filter(sale=True)
        else:
            return self.model.objects.filter(manager=user, sale=True)

    def has_add_permission(self, request, obj=None):
        return False

    list_display = ('name', 'phone', 'mail', 'created', 'price', 'ticket_comment')
    list_filter = ['mail', 'created', 'status', 'manager']
    search_fields = ['mail', 'manager']
    date_hierarchy = 'created'
    readonly_fields = ('country', 'city', 'time_zone')
    fields = ('name', 'phone', 'mail', 'country', 'city', 'time_zone', 'manager', 'ticket_comment', 'price')
    form = SaleAdminForm


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Sale, SaleAdmin)
