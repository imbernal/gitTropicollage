# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20160226_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservacion',
            name='phone_nombre',
            field=models.IntegerField(default=0),
        ),
    ]
