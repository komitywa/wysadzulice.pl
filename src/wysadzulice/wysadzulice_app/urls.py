# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^campaigns/new$', views.new_campaign, name='new_campaign'),
    url(r'^campaigns/create$', views.create_campaign, name='create_campaign'),
    url(r'^campaigns/(?P<id_>[0-9]+)$', views.show_campaign, name='show_campaign'),
    url(r'^campaigns/new_planting/(?P<id_>[0-9]+)$', views.new_planting, name='new_planting'),
    url(r'^campaigns/create_planting/(?P<id_>[0-9]+)$', views.create_planting, name='create_planting'),
]
