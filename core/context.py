import datetime
from core.models import Setup

__author__ = 'alexy'


def site_setup(request):
    try:
        qss = Setup.objects.all().first()
    except:
        qss = None
    return {
        'SETUP': qss,
    }
