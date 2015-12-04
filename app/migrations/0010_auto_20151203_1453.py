# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20151202_2144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='correo',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='usuario',
            new_name='full_name',
        ),
        migrations.AddField(
            model_name='feedback',
            name='ip_address',
            field=models.GenericIPAddressField(default=None),
        ),
        migrations.AddField(
            model_name='feedback',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 12, 3, 14, 53, 51, 200801, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
