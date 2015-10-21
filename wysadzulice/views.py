# -*- coding: utf-8 -*-

import json

from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import models


def index(request):
    return redirect('new_campaign')


def new_campaign(request):
    return render(request, 'new_campaign.html')


def create_campaign(request):
    c = models.Campaign()
    c.save()
    return redirect('show_campaign', id_=str(c.id))


def show_campaign(request, id_):
    c = models.Campaign.objects.filter(id=id_)
    p = models.Planting.objects.filter(campaign=c)
    return render(request, 'show_campaign.html', context={
        'id_': id_,
        'plantings': p,
    })


def new_planting(request, id_):
    return render(request, 'new_planting.html', context={'id_': id_})


@csrf_exempt
def create_planting(request, id_):
    c = models.Campaign.objects.get(id=id_)
    planting = json.loads(request.body.decode("utf-8"))
    objects = planting['objects']

    p = models.Planting(
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
        o = models.PlantedObject(
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
