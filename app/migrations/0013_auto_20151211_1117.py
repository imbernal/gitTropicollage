# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0012_auto_20151207_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservacion',
            name='hora_estimada',
            field=models.CharField(default='', max_length=50),
        ),
    ]
