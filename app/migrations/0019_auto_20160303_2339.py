# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20160303_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservacion',
            name='hab_dobles',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='hab_simples',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='hab_triples',
            field=models.CharField(default='', max_length=50),
        ),
    ]
