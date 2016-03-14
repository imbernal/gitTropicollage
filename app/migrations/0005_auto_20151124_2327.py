# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0004_delete_upload_json'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habitacion',
            name='camaMatrimonial',
        ),
        migrations.RemoveField(
            model_name='habitacion',
            name='camaTresCuarto',
        ),
        migrations.RemoveField(
            model_name='habitacion',
            name='cant_infantes',
        ),
        migrations.RemoveField(
            model_name='habitacion',
            name='cant_ninos',
        ),
        migrations.RemoveField(
            model_name='habitacion',
            name='cantidad_adultos',
        ),
    ]
