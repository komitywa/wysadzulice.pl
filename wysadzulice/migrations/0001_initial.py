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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField()),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Planting',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('campaign', models.ForeignKey(to='wysadzulice.Campaign')),
            ],
        ),
        migrations.AddField(
            model_name='plantedobject',
            name='planting',
            field=models.ForeignKey(to='wysadzulice.Planting'),
        ),
    ]
