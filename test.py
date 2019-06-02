# coding=utf-8
from django.http import HttpResponse


def index_view(request):
    return HttpResponse('hello git!')


print ("githab上添加的")


print("本地库添加的")
