# coding=utf-8
from django.http import HttpResponse


def index_view(request):
    return HttpResponse('hello git!')


print("githab上添加的")

print("本地库添加的")

print("提交到dev分支")

print("测试本地pull拉去")

print("本地提交")
