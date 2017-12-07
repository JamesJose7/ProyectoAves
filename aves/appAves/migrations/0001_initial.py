# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='autor',
            fields=[
                ('id_autor', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ave',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('codigo', models.CharField(max_length=200)),
                ('especie', models.CharField(max_length=200)),
                ('synonim', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('morfometres', models.CharField(max_length=200)),
                ('ecology', models.CharField(max_length=200)),
                ('behaviour', models.CharField(max_length=200)),
                ('yearPublished', models.CharField(max_length=200)),
                ('yearCollection', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('call', models.CharField(max_length=200)),
                ('observacion', models.CharField(max_length=200)),
                ('id_autor', models.ForeignKey(to='appAves.autor')),
            ],
        ),
        migrations.CreateModel(
            name='bibliografia',
            fields=[
                ('id_bilbiografia', models.AutoField(serialize=False, primary_key=True)),
                ('bibliografia', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='endemismo',
            fields=[
                ('id_endemismo', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='familia',
            fields=[
                ('id_familia', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('orden', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='migracion',
            fields=[
                ('id_migracion', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ubicacion',
            fields=[
                ('id_ubicacion', models.AutoField(serialize=False, primary_key=True)),
                ('pais', models.CharField(max_length=200)),
                ('provincia', models.CharField(max_length=200)),
                ('localidad', models.CharField(max_length=200)),
                ('toponim', models.CharField(max_length=200)),
                ('longitud', models.CharField(max_length=200)),
                ('latitud', models.CharField(max_length=200)),
                ('gps', models.CharField(max_length=200)),
                ('latitudMax', models.CharField(max_length=200)),
                ('latitudMin', models.CharField(max_length=200)),
                ('id_ave', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='uicn',
            fields=[
                ('id_familia', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='ave',
            name='id_bibliografia',
            field=models.ForeignKey(to='appAves.bibliografia'),
        ),
        migrations.AddField(
            model_name='ave',
            name='id_endemismo',
            field=models.ForeignKey(to='appAves.endemismo'),
        ),
        migrations.AddField(
            model_name='ave',
            name='id_familia',
            field=models.ForeignKey(to='appAves.familia'),
        ),
        migrations.AddField(
            model_name='ave',
            name='id_migracion',
            field=models.ForeignKey(to='appAves.migracion'),
        ),
    ]
