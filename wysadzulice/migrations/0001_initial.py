# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('zoom', models.FloatField()),
                ('heading', models.FloatField()),
                ('pitch', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PlantedObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('object_id', models.IntegerField()),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('width', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Planting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('campaign', models.ForeignKey(to='wysadzulice.Campaign')),
            ],
        ),
        migrations.AddField(
            model_name='plantedobject',
            name='planting',
            field=models.ForeignKey(to='wysadzulice.Planting'),
        ),
    ]
