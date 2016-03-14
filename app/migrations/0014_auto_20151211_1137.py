# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0013_auto_20151211_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservacion',
            name='hora_estimada',
            field=models.TimeField(default=None),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='phone_nombre',
            field=models.IntegerField(default=''),
        ),
    ]
