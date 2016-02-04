# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20151206_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservacion',
            name='hora_estimada',
            field=models.TimeField(),
        ),
    ]
