# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class Campaign(models.Model):
    pass


class Planting(models.Model):
    campaign = models.ForeignKey(Campaign)
