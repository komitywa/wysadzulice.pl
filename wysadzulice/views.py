# -*- coding: utf-8 -*-

import json

from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from wysadzulice.models import Campaign
from wysadzulice.models import CatalogItem
from wysadzulice.models import Mail
from wysadzulice.models import PlantedObject
from wysadzulice.models import Planting


def mailing(request):
    if request.method == 'POST':
        Mail(email=request.POST['email']).save()
        return redirect('mailing')
    return render(request, 'mailing.html')


def index(request):
    campaigns = Campaign.objects.all()
    return render(request, 'index.html', context={
        'campaigns': campaigns,
    })


@csrf_exempt
def new_campaign(request):
    if request.method == 'POST' and request.is_ajax:
        campaign_data = json.loads(request.body.decode('utf-8'))
        items = campaign_data.pop('checked')
        campaign = Campaign(**campaign_data)
        campaign.save()
        campaign.items.add(*CatalogItem.objects.filter(
            catalog_id__in=items))
        return HttpResponse('{"url": "%s"}' % reverse(
            'show_campaign',
            kwargs={'id_': str(campaign.id)}))
    return render(request, 'new_campaign.html', context={
        'google_maps_key': settings.GOOGLE_MAPS_KEY,
    })


def show_campaign(request, id_):
    campaign = Campaign.objects.get(id=id_)
    plantings = Planting.objects.filter(campaign=campaign)
    return render(request, 'show_campaign.html', context={
        'campaign': campaign,
        'plantings': plantings,
    })


@csrf_exempt
def new_planting(request, id_):
    campaign = Campaign.objects.get(id=id_)
    if request.method == 'POST' and request.is_ajax:
        planting = Planting(campaign=campaign)
        planting.save()
        planting_data = json.loads(request.body.decode('utf-8'))
        objects = planting_data['objects']
        for o in objects.values():
            PlantedObject(
                planting=planting, object_id=o['objectId'], x=o['x'], y=o['y'],
                scale=o['scale']).save()
        return HttpResponse('{"url": "%s"}' % reverse(
            'show_planting',
            kwargs={'campaign_id': id_, 'planting_id': planting.id}))
    return render(request, 'new_planting.html', context={
        'google_maps_key': settings.GOOGLE_MAPS_KEY,
        'campaign': campaign,
    })


def show_planting(request, campaign_id, planting_id):
    campaign = Campaign.objects.get(id=campaign_id)
    planting = Planting.objects.get(id=planting_id)
    planted_objects = PlantedObject.objects.filter(planting=planting)
    return render(request, 'show_planting.html', context={
        'google_maps_key': settings.GOOGLE_MAPS_KEY,
        'campaign': campaign,
        'planting': planting,
        'planted_objects': planted_objects,
    })


def catalog(request):
    items = CatalogItem.objects.order_by('id')
    return render(request, 'catalog.json', context={'items': items})


def manifesto(request, id_):
    items = Campaign.objects.get(id=id_).items.order_by('id')
    return render(request, 'manifesto.json', context={'items': items})
