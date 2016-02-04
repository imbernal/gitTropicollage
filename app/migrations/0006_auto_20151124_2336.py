# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20151124_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='casa',
            name='precio_alta',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='casa',
            name='precio_baja',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='casa',
            name='tempAltaFin',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='casa',
            name='tempAltaIni',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='casa',
            name='tempBajaFin',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='casa',
            name='tempBajaIni',
            field=models.DateField(null=True),
        ),
    ]
