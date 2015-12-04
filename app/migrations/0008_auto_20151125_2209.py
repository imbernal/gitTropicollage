# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20151125_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casa',
            name='telefono',
            field=models.NullBooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')]),
        ),
    ]
