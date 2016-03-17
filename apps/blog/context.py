import datetime
from .models import PostSection

__author__ = 'alexy'


def postsection_list(request):
    qs = PostSection.objects.all()
    return {
        'POSTSECTION_LIST': qs
    }
