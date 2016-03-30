# -*- coding: utf-8 -*-

from django.db import models


class Mail(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


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
    scale = models.FloatField()
