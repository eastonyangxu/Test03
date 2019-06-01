from django.shortcuts import render
from .models import *
import math


# Create your views here.
def page(num, size=20):
    # 接收当前页码数
    num = int(num)
    # 总记录数
    count = Movie.objects.count()
    # 总页数
    pages = int(math.ceil(count * 1.0 / size))
    # 判断是否越界
    if num < 1:
        num = 1
    elif num > pages:
        num = pages

    # 计算每页显示的记录
    movies = Movie.objects.all()[(num - 1) * size:num * size]

    return movies, num


# 原生分页
def index_view(request):
    # 接收请求参数 num
    num = request.GET.get('num', 1)
    # 处理分页请求
    movies, n = page(num)

    # 上一页的页码
    pre_page_num = n - 1
    # 下一页的页码
    next_page_num = n + 1

    return render(request, 'index01.html',
                  {'movies': movies, 'pre_page_num': pre_page_num, 'next_page_num': next_page_num})


from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# django分页
def index2_view(request):
    # 获取当前页码数
    num = request.GET.get('num', 1)
    n = int(num)
    # 查询所有数据
    movies = Movie.objects.all()
    # 创建分页器对象
    pager = Paginator(movies, 20)
    # 获取当前页的数据
    try:
        perpage_data = pager.page(n)
    except PageNotAnInteger:
        # 返回第一页的数据
        perpage_data = pager.page(1)
    except EmptyPage:
        # 返回最后一页的数据
        perpage_data = pager.page(pager.num_pages)

    # 每页开始页码
    begin = (n - int(math.ceil(10.0 / 2)))
    if begin < 1:
        begin = 1
    # 每页结束页码
    end = begin + 9
    if end > pager.num_pages:
        end = pager.num_pages
    if end <= 10:
        begin = 1
    else:
        begin = end - 9

    pagelist = range(begin, end + 1)

    return render(request, 'index01.html',
                  {'pager': pager, 'perpage_data': perpage_data, 'pagelist': pagelist, 'currentPage': n})
