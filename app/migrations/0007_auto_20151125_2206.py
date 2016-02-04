# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20151124_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casa',
            name='otra_informacion',
            field=models.TextField(max_length=600),
        ),
    ]
