# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wysadzulice', '0003_mail'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('image', models.CharField(max_length=250)),
                ('catalog_id', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='campaign',
            name='items',
            field=models.ManyToManyField(to='wysadzulice.CatalogItem'),
        ),
    ]
