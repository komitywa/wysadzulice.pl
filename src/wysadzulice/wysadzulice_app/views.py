# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

from . import models


def index(request):
    return HttpResponse(u"Welcome on wysadzulice.pl")


def new_campaign(request):
    return render(request, 'new_campaign.html')


def create_campaign(request):
    c = models.Campaign()
    c.save()
    return redirect('show_campaign', id_=str(c.id))


def show_campaign(request, id_):
    return HttpResponse(u"That's a view for camapaign with id %s." % id_)
