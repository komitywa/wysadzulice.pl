# -*- coding: utf-8 -*-

import json

from django.core.urlresolvers import reverse
from django.http import HttpResponse
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
    campaign = Campaign.objects.get(id=id_)
    return render(request, 'show_campaign.html', context={
        'campaign': campaign,
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
                planting=planting, object_id=o['objectId'], x=o['x'], y=o['y']
            ).save()
        return HttpResponse('{"url": "%s"}' % reverse(
            'show_planting',
            kwargs={'campaign_id': id_, 'planting_id': planting.id}))
    return render(request, 'new_planting.html', context={
        'campaign': campaign,
    })


def list_plantings(request, id_):
    campaign = Campaign.objects.get(id=id_)
    plantings = Planting.objects.filter(campaign=campaign)
    return render(request, 'list_plantings.html', context={
        'campaign': campaign,
        'plantings': plantings,
    })


def show_planting(request, campaign_id, planting_id):
    campaign = Campaign.objects.get(id=campaign_id)
    planting = Planting.objects.get(id=planting_id)
    planted_objects = PlantedObject.objects.filter(planting=planting)
    return render(request, 'show_planting.html', context={
        'campaign': campaign,
        'planting': planting,
        'planted_objects': planted_objects,
    })
