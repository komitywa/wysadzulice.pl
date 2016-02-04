# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wysadzulice', '0002_auto_20160204_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plantedobject',
            name='layer',
        ),
        migrations.RemoveField(
            model_name='plantedobject',
            name='projection',
        ),
        migrations.RemoveField(
            model_name='plantedobject',
            name='scale',
        ),
        migrations.RemoveField(
            model_name='planting',
            name='heading',
        ),
        migrations.RemoveField(
            model_name='planting',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='planting',
            name='lng',
        ),
        migrations.RemoveField(
            model_name='planting',
            name='manifesto',
        ),
        migrations.RemoveField(
            model_name='planting',
            name='pitch',
        ),
        migrations.RemoveField(
            model_name='planting',
            name='zoom',
        ),
    ]
