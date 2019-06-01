# coding = utf-8

from django.conf.urls import url
import movie.views as views

urlpatterns = [
    url(r'^$', views.index_view),
    url(r'^index/$', views.index2_view),
]
