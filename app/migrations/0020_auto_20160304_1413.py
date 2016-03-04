# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20160303_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservacion',
            name='hora_estimada',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
