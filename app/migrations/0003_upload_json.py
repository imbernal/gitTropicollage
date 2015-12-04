# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151122_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload_json',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
