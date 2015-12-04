# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(default='', max_length=255)),
                ('direccion_postal', models.CharField(default='', max_length=255)),
                ('municipio', models.CharField(default='', max_length=255)),
                ('provincia', models.CharField(default='', max_length=255)),
                ('pais', models.CharField(default='', max_length=255)),
                ('polo_turistico', models.CharField(default='', max_length=255)),
                ('cant_habitaciones', models.PositiveIntegerField()),
                ('ninos_enCasa', models.BooleanField(default=False)),
                ('mascotas_enCasa', models.BooleanField(default=False)),
                ('mensaje_promocional', models.TextField(max_length=600)),
                ('foto_principal', models.FileField(upload_to='imagenes', verbose_name='foto_principal')),
                ('desayuno', models.BooleanField(default=False)),
                ('meriendas', models.BooleanField(default=False)),
                ('cena', models.BooleanField(default=False)),
                ('bebidas_bar', models.BooleanField(default=False)),
                ('telefono', models.CharField(default='', max_length=255)),
                ('garaje', models.CharField(default='', max_length=255)),
                ('jacuzzi', models.CharField(default='', max_length=255)),
                ('piscina', models.CharField(default='', max_length=255)),
                ('cuidador_Nino', models.CharField(default='', max_length=255)),
                ('gimnasio', models.CharField(default='', max_length=255)),
                ('internet', models.CharField(default='', max_length=255)),
                ('parqueo', models.BooleanField()),
                ('clase_baile', models.BooleanField()),
                ('lavanderia', models.BooleanField()),
                ('comida_vegetariana', models.BooleanField()),
                ('pantry', models.BooleanField()),
                ('nombre_dueno', models.CharField(max_length=255)),
                ('correo', models.CharField(default='', max_length=255)),
                ('telf', models.CharField(max_length=255)),
                ('celular', models.CharField(max_length=255)),
                ('foto_dueno', models.FileField(upload_to='imagenes', verbose_name='foto_dueno')),
                ('superhost', models.NullBooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')])),
                ('categoria', models.PositiveIntegerField(blank=True, null=True)),
                ('ingles', models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')])),
                ('frances', models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')])),
                ('aleman', models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')])),
                ('italiano', models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')])),
                ('portugues', models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')])),
                ('otra_informacion', models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')])),
                ('permiten_ninos', models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')])),
                ('permiten_mascotas', models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')])),
                ('ciudad', models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')])),
                ('campo', models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')])),
                ('playa', models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')])),
            ],
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('usuario', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('body', models.TextField(max_length=600)),
                ('casa', models.ForeignKey(to='app.Casa')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(verbose_name='Title', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Galleries',
            },
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('precio_alta', models.FloatField(default=0)),
                ('precio_baja', models.FloatField(default=0)),
                ('cant_infantes', models.PositiveIntegerField(default=0)),
                ('cant_ninos', models.PositiveIntegerField(default=0)),
                ('cantidad_adultos', models.PositiveIntegerField(default=0)),
                ('cama_personal', models.PositiveIntegerField(default=0)),
                ('cama_doble', models.PositiveIntegerField(default=0)),
                ('camaTresCuarto', models.PositiveIntegerField(default=0)),
                ('camaMatrimonial', models.PositiveIntegerField(default=0)),
                ('primer_piso', models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')])),
                ('segundo_piso', models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')])),
                ('superior', models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')])),
                ('caja_fuerte', models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')])),
                ('ventilador', models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')])),
                ('aire_acondicionado', models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')])),
                ('agua_caliente', models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')])),
                ('secador', models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')])),
                ('minibar', models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')])),
                ('corriente_110', models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')])),
                ('corriente_220', models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')])),
                ('balcon', models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')])),
                ('terraza', models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')])),
                ('bano_privado', models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')])),
                ('TV', models.BooleanField(choices=[(None, 'All'), (True, 'Yes'), (False, 'No')])),
                ('casa', models.ForeignKey(to='app.Casa')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('file', models.FileField(upload_to='imagenes/', verbose_name='File')),
                ('gallery', models.ForeignKey(blank=True, null=True, related_name='images', to='app.Gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('fecha_ini', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('casa', models.ForeignKey(to='app.Casa')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='casa',
            name='gallery',
            field=models.OneToOneField(to='app.Gallery'),
        ),
    ]
