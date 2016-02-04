# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20151125_2209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservacion',
            name='user',
        ),
        migrations.AddField(
            model_name='reservacion',
            name='cant_habitacion',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reservacion',
            name='city_town',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='reservacion',
            name='comment',
            field=models.TextField(max_length=600, default=''),
        ),
        migrations.AddField(
            model_name='reservacion',
            name='country',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='reservacion',
            name='email',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='reservacion',
            name='first_name',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='reservacion',
            name='forma_llegada',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='reservacion',
            name='hab_dobles',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reservacion',
            name='hab_simples',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reservacion',
            name='hab_triples',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reservacion',
            name='hora_estimada',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='reservacion',
            name='last_name',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='reservacion',
            name='phone_nombre',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AlterField(
            model_name='casa',
            name='aleman',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='campo',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='ciudad',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='clase_baile',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='comida_vegetariana',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='cuidador_Nino',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='frances',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='garaje',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='gimnasio',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='ingles',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='internet',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='italiano',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='jacuzzi',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='lavanderia',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='pantry',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='parqueo',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='permiten_mascotas',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='permiten_ninos',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='piscina',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='playa',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='portugues',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='superhost',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='casa',
            name='telefono',
            field=models.NullBooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='TV',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='agua_caliente',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='aire_acondicionado',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='balcon',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='bano_privado',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='caja_fuerte',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='corriente_110',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='corriente_220',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='minibar',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='primer_piso',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='secador',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='segundo_piso',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='superior',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='terraza',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='ventilador',
            field=models.BooleanField(choices=[(None, 'All'), (True, 'Yes')]),
        ),
    ]
