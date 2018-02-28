# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenazas',
            fields=[
                ('idamenaza', models.AutoField(serialize=False, primary_key=True)),
                ('clasificacion', models.CharField(max_length=3, unique=True, null=True, blank=True)),
            ],
            options={
                'db_table': 'amenazas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('idautor', models.AutoField(serialize=False, primary_key=True)),
                ('autor', models.CharField(unique=True, max_length=25)),
                ('bibliografia', models.CharField(max_length=445, null=True, blank=True)),
                ('a_opublicacion', models.CharField(max_length=8, null=True, db_column='a\xf1opublicacion', blank=True)),
                ('a_orecoleccion', models.CharField(max_length=10, null=True, db_column='a\xf1orecoleccion', blank=True)),
                ('fecha', models.CharField(max_length=35, null=True, blank=True)),
            ],
            options={
                'db_table': 'autores',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AutoresAves',
            fields=[
                ('idestudio', models.AutoField(serialize=False, primary_key=True)),
                ('fuente', models.CharField(max_length=15, null=True, blank=True)),
            ],
            options={
                'db_table': 'autores_aves',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Aves',
            fields=[
                ('codigo', models.AutoField(serialize=False, primary_key=True)),
                ('codigoespecie', models.CharField(unique=True, max_length=10)),
                ('clase', models.CharField(max_length=4)),
                ('namebird', models.CharField(max_length=35, null=True, blank=True)),
                ('sinonimo', models.CharField(max_length=55, null=True, blank=True)),
                ('utm_wgs', models.CharField(max_length=3, null=True, blank=True)),
                ('utm_zone', models.CharField(max_length=17, null=True, blank=True)),
                ('migracion', models.CharField(max_length=15)),
                ('endemica', models.CharField(max_length=15)),
                ('morfometrica', models.CharField(max_length=3, null=True, blank=True)),
                ('ecologia', models.CharField(max_length=3, null=True, blank=True)),
                ('comportamiento', models.CharField(max_length=3, null=True, blank=True)),
                ('llamada', models.CharField(max_length=3, null=True, blank=True)),
                ('observacion', models.CharField(max_length=400, null=True, blank=True)),
            ],
            options={
                'db_table': 'aves',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Denominacion',
            fields=[
                ('iddenominacion', models.AutoField(serialize=False, primary_key=True)),
                ('ordenclade', models.CharField(unique=True, max_length=25)),
            ],
            options={
                'db_table': 'denominacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Especies',
            fields=[
                ('idespecie', models.AutoField(serialize=False, primary_key=True)),
                ('nombespecie', models.CharField(unique=True, max_length=35)),
            ],
            options={
                'db_table': 'especies',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EspeciesAves',
            fields=[
                ('idclasificacion', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'especies_aves',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Familias',
            fields=[
                ('idfamilia', models.AutoField(serialize=False, primary_key=True)),
                ('nombfamilia', models.CharField(unique=True, max_length=20)),
            ],
            options={
                'db_table': 'familias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Localidades',
            fields=[
                ('idlocalidad', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=75)),
            ],
            options={
                'db_table': 'localidades',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LocalidadesAves',
            fields=[
                ('idlocal', models.AutoField(serialize=False, primary_key=True)),
                ('ecosistema', models.CharField(max_length=75)),
                ('nombftecoord', models.CharField(max_length=5, null=True, blank=True)),
                ('toponim', models.CharField(max_length=30, null=True, blank=True)),
                ('latitud', models.CharField(max_length=15)),
                ('longitud', models.CharField(max_length=15)),
                ('altitud', models.CharField(max_length=15)),
                ('altitudmax', models.CharField(max_length=15)),
                ('altitudmin', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'localidades_aves',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Paises',
            fields=[
                ('idpais', models.CharField(max_length=3, serialize=False, primary_key=True)),
                ('nombpais', models.CharField(max_length=60, unique=True, null=True, blank=True)),
            ],
            options={
                'db_table': 'paises',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Provincias',
            fields=[
                ('idpro', models.AutoField(serialize=False, primary_key=True)),
                ('nombprovincia', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'db_table': 'provincias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('idurl', models.AutoField(serialize=False, primary_key=True)),
                ('url', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'urls',
                'managed': False,
            },
        ),
    ]
