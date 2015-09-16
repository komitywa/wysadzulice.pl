# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlantedObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.IntegerField()),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('scale', models.FloatField()),
                ('layer', models.IntegerField()),
                ('projection', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Planting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('zoom', models.FloatField()),
                ('heading', models.FloatField()),
                ('pitch', models.FloatField()),
                ('manifesto', models.CharField(max_length=200)),
                ('campaign', models.ForeignKey(to='wysadzulice_app.Campaign')),
            ],
        ),
        migrations.AddField(
            model_name='plantedobject',
            name='planting',
            field=models.ForeignKey(to='wysadzulice_app.Planting'),
        ),
    ]
