# coding=utf-8
import urllib

from django.conf import settings
import urllib2
import json
from core.geotagging import url_fix

__author__ = 'alexy'


class PhoneGeocode(object):
    """
    Получение геоданных по номеру сотового телефона
    """
    def __init__(self, phone=None):
        self.api_key = getattr(settings, 'HTMLWEB_API_KEY', None)
        self.phone = phone
        self.url = u'http://htmlweb.ru/geo/api.php'

    def phone_format(self):
        result_phone = ''
        if self.phone:
            for i in self.phone:
                if i.isdigit():
                    result_phone += i
        else:
            result_phone = False
        if len(result_phone) != 11:
            result_phone = False
        return result_phone

    def get_info(self):
        data = None
        if self.api_key and self.phone_format():
            url = url_fix('http://htmlweb.ru/geo/api.php?json&charset=utf-8&telcod=%s&api_key=%s' %
                          (self.phone_format(), self.api_key))
            f = urllib2.urlopen(url)
            response = f.read()
            try:
                data = json.loads(response)
            except ValueError:
                data = None
        return data
