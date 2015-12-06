# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20151203_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='casa',
            name='filter_agua_caliente',
            field=models.BooleanField(default=False, choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AddField(
            model_name='casa',
            name='filter_bano_privado',
            field=models.BooleanField(default=False, choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AddField(
            model_name='casa',
            name='filter_caja_fuerte',
            field=models.BooleanField(default=False, choices=[(None, 'All'), (True, 'Yes')]),
        ),
    ]
