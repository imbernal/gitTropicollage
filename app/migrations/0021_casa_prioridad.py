# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20160304_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='casa',
            name='prioridad',
            field=models.CharField(null=True, max_length=255),
        ),
    ]
