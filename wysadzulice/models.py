# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class Campaign(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    zoom = models.FloatField()
    heading = models.FloatField()
    pitch = models.FloatField()


class Planting(models.Model):
    campaign = models.ForeignKey(Campaign)


class PlantedObject(models.Model):
    planting = models.ForeignKey(Planting)
    object_id = models.IntegerField()
    x = models.FloatField()
    y = models.FloatField()
    width = models.FloatField()
