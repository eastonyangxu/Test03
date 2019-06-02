# coding=utf-8
from django.http import HttpResponse


def add_view(request):
    dict = request.GET.dict()
    return HttpResponse('dict=%s' % dict)
