from annoying.decorators import ajax_request
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from apps.ticket.forms import TicketForm
from apps.ticket.models import Ticket


def ticket_send(request):
    if request.method == "POST":
        form = TicketForm(data=request.POST)
        theme = request.POST.get('theme')
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.status = 1
            ticket.theme = int(theme)
            ticket.save()
    return HttpResponseRedirect(reverse('landing:thnx'))


def mail_read(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.mail_view = True
    ticket.save()
    file = 'check.png'
    image = '%s%s' % (settings.STATIC_URL, file)
    return HttpResponse(image)
