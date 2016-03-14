# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casa',
            name='clase_baile',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='comida_vegetariana',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='cuidador_Nino',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='garaje',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='gimnasio',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='internet',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='jacuzzi',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='lavanderia',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='pantry',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='parqueo',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='piscina',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='superhost',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')],
                                      default=datetime.datetime(2015, 11, 22, 11, 59, 45, 535065, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
