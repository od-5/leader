# coding=utf-8
from annoying.decorators import ajax_request
from django.shortcuts import get_object_or_404
from core.models import User


__author__ = 'alexy'


# @ajax_request
# def ymap(request):
#     request.encoding = 'utf-8'
#     if request.is_ajax():
#         query = City.objects.all()
#         try:
#             if request.user.type == 2:
#                 query = query.filter(moderator=request.user)
#         except:
#             pass
#         result = []
#         for item in query:
#             result_json = {}
#             result_json['name'] = u'%s (%s)' % (item.name, item.surface_count())
#             result_json['coord_x'] = float(item.coord_x)
#             result_json['coord_y'] = float(item.coord_y)
#             result.append(result_json)
#         data = result
#     else:
#         data = {'msg': 'fail'}
#     return data
