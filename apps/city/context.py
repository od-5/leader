import datetime
from .models import City

__author__ = 'alexy'


def city_list(request):
    qs = City.objects.all()
    return {
        'CITY_LIST': qs
    }
