# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('id_autor', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('bibliografia', models.CharField(max_length=200, null=True)),
                ('fecha', models.CharField(max_length=200, null=True)),
                ('year_of_collection', models.CharField(max_length=200, null=True)),
                ('year_of_public', models.CharField(max_length=200, null=True)),
                ('source', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'Autores',
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
                'default_related_name': 'Autor',
            },
        ),
        migrations.CreateModel(
            name='Ave',
            fields=[
                ('id_ave', models.AutoField(serialize=False, primary_key=True)),
                ('codigo', models.CharField(max_length=200, null=True)),
                ('especie', models.CharField(max_length=200, null=True)),
                ('synonim', models.CharField(max_length=200, null=True)),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('morfometria', models.CharField(max_length=200, null=True)),
                ('ecologia', models.CharField(max_length=200, null=True)),
                ('comportamiento', models.CharField(max_length=200, null=True)),
                ('clase', models.CharField(max_length=200, null=True)),
                ('llamar', models.CharField(max_length=200, null=True)),
                ('uicn', models.CharField(max_length=200, null=True)),
                ('endemismo', models.CharField(max_length=200, null=True)),
                ('observacion', models.CharField(max_length=200, null=True)),
                ('migracion', models.CharField(max_length=200, null=True)),
                ('ecosistema', models.CharField(max_length=200, null=True)),
                ('id_autor', models.ForeignKey(to='appAves.Autores')),
            ],
            options={
                'db_table': 'Ave',
                'verbose_name': 'Ave',
                'verbose_name_plural': 'Aves',
                'default_related_name': 'Ave',
            },
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id_familia', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('orden', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'Familia',
                'verbose_name': 'Familia',
                'verbose_name_plural': 'Familias',
                'default_related_name': 'Familia',
            },
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id_localidad', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('toponim', models.CharField(max_length=200, null=True)),
                ('pais', models.CharField(max_length=200, null=True)),
                ('provincia', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'Localidad',
                'verbose_name': 'Localidad',
                'verbose_name_plural': 'Localidades',
                'default_related_name': 'Localidad',
            },
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id_ubicacion', models.AutoField(serialize=False, primary_key=True)),
                ('cordinate', models.CharField(max_length=200, null=True)),
                ('altitudmax', models.CharField(max_length=200, null=True, db_column='altitudMax')),
                ('altitudmin', models.CharField(max_length=200, null=True, db_column='altitudMin')),
                ('utmwgs', models.CharField(max_length=200, null=True)),
                ('longitudy', models.CharField(max_length=200, null=True, db_column='longitudY')),
                ('latitudx', models.CharField(max_length=200, null=True, db_column='latitudX')),
                ('id_localidad', models.ForeignKey(to='appAves.Localidad')),
            ],
            options={
                'db_table': 'Ubicacion',
                'verbose_name': 'Ubicacion',
                'verbose_name_plural': 'Ubicaciones',
                'default_related_name': 'Ubicacion',
            },
        ),
        migrations.AddField(
            model_name='ave',
            name='id_familia',
            field=models.ForeignKey(to='appAves.Familia'),
        ),
        migrations.AddField(
            model_name='ave',
            name='id_ubicacion',
            field=models.ForeignKey(to='appAves.Ubicacion'),
        ),
    ]
