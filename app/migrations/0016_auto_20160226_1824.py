# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 18:24
from __future__ import unicode_literals

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_casa_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casa',
            name='foto_dueno',
            field=versatileimagefield.fields.VersatileImageField(upload_to='imagenes', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='casa',
            name='foto_principal',
            field=versatileimagefield.fields.VersatileImageField(upload_to='imagenes', verbose_name='Image'),
        ),
    ]