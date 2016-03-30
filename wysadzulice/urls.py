# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.mailing, name='mailing'),
    url(r'^campaigns$', views.index, name='index'),
    url(r'^campaigns/new$', views.new_campaign, name='new_campaign'),
    url(
        r'^campaigns/(?P<id_>[0-9]+)$',
        views.show_campaign,
        name='show_campaign',
    ),
    url(
        r'^campaigns/(?P<id_>[0-9]+)/plantings/new$',
        views.new_planting,
        name='new_planting',
    ),
    url(
        r'^campaigns/(?P<campaign_id>[0-9]+)'
        r'/plantings/(?P<planting_id>[0-9]+)$',
        views.show_planting,
        name='show_planting',
    ),
]
