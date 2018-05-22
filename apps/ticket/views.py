import csv

from annoying.decorators import ajax_request
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from apps.ticket.forms import TicketForm
from apps.ticket.models import Ticket


def ticket_send(request):
    if request.method == "POST":
        form = TicketForm(data=request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.status = 1
            ticket.save()
    return HttpResponseRedirect(reverse('landing:thnx'))


def mail_read(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.mail_view = True
    ticket.save()
    file = 'check.png'
    image = '%s%s' % (settings.STATIC_URL, file)
    return HttpResponse(image)


@login_required
def ticket_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    qs = Ticket.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    for i in qs:
        # try:
        writer.writerow([i.name.encode('utf8'), i.phone, i.mail])
        # except:
        #     pass

    return response
