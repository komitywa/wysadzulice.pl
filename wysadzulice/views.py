# -*- coding: utf-8 -*-

import json

from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Campaign
from .models import PlantedObject
from .models import Planting


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def new_campaign(request):
    if request.method == 'POST' and request.is_ajax:
        campaign_data = json.loads(request.body.decode('utf-8'))
        campaign = Campaign(**campaign_data)
        campaign.save()
        return HttpResponse('{"url": "%s"}' % reverse(
            'show_campaign',
            kwargs={'id_': str(campaign.id)}))
    return render(request, 'new_campaign.html')


def list_campaigns(request):
    campaigns = Campaign.objects.all()
    return render(request, 'list_campaigns.html', context={
        'campaigns': campaigns,
    })


def show_campaign(request, id_):
    c = Campaign.objects.filter(id=id_)
    p = Planting.objects.filter(campaign=c)
    return render(request, 'show_campaign.html', context={
        'id_': id_,
        'plantings': p,
    })


def new_planting(request, id_):
    return render(request, 'new_planting.html', context={'id_': id_})


@csrf_exempt
def create_planting(request, id_):
    c = Campaign.objects.get(id=id_)
    planting = json.loads(request.body.decode("utf-8"))
    objects = planting['objects']

    p = Planting(
        campaign=c,
        lat=planting.get('lat', 0),
        lng=planting.get('lng', 0),
        zoom=planting.get('zoom', 1),
        heading=planting.get('heading', 0) or 0,
        pitch=planting.get('pitch', 0),
        manifesto=planting.get('manifesto', ''),
    )

    p.save()

    for obj in objects.values():
        o = PlantedObject(
            planting=p,
            object_id=obj.get('object_id', 0),
            x=obj.get('x', 0),
            y=obj.get('y', 0),
            scale=obj.get('scale', 1),
            layer=obj.get('layer', 1),
            projection=obj.get('projection', 0),
        )
        o.save()
    return HttpResponse(u'{"url": "%s"}' % reverse(
        'show_campaign',
        kwargs=dict(id_=id_)
    ))
