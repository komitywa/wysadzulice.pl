# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wysadzulice_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('campaign', models.ForeignKey(to='wysadzulice_app.Campaign')),
            ],
        ),
    ]
