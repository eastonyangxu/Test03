# coding = utf-8

from django.conf.urls import url
import movie.views as views
import movie.add as add

urlpatterns = [
    url(r'^$', views.index_view),
    url(r'^index/$', views.index2_view),
    url(r'^add/$', add.add_view),
]
