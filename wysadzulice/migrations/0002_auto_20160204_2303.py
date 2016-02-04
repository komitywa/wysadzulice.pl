# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wysadzulice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='heading',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='campaign',
            name='lat',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='campaign',
            name='lng',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='campaign',
            name='pitch',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='campaign',
            name='zoom',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
