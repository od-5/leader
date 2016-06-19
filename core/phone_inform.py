# coding=utf-8
from django.conf import settings
import urllib2
import json
from core.geotagging import url_fix

__author__ = 'alexy'


api_key = settings.HTMLWEB_API_KEY


def format_phone(phone):
    delim = ['+', '(', ')', '-', ' ']
    for i in delim:
        phone = phone.replace(i, '')
    return phone


def get_JSON_data(phone, key):
    url = url_fix('http://htmlweb.ru/geo/api.php?json&charset=utf-8&telcod=%s&api_key=%s' % (phone, key))
    f = urllib2.urlopen(url)
    return f.read()


def getphoneObject(phone, key):
    formated_phone = format_phone(phone)
    response = get_JSON_data(formated_phone, key)
    data = json.loads(response)
    return data

# def geocode(key, address):
#     response = getpointGeoObject(address, key)
#     pos = list(response)[0].split(' ')
#     return pos
