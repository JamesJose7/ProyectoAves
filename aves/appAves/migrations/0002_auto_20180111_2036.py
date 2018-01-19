# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appAves', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='lugares',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('longitud', models.CharField(max_length=100)),
                ('latidud', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='autores',
            name='bibliografia',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='autores',
            name='fecha',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='autores',
            name='nombre',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='autores',
            name='source',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='autores',
            name='year_of_collection',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='autores',
            name='year_of_public',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='ave',
            name='clase',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='ave',
            name='codigo',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='ave',
            name='comportamiento',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='ave',
            name='ecologia',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='ave',
            name='ecosistema',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='ave',
            name='endemismo',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='ave',
            name='especie',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='ave',
            name='llamar',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='ave',
            name='migracion',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='ave',
            name='morfometria',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='ave',
            name='nombre',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='ave',
            name='observacion',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='ave',
            name='synonim',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='ave',
            name='uicn',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='familia',
            name='nombre',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='familia',
            name='orden',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='localidad',
            name='nombre',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='localidad',
            name='pais',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='localidad',
            name='provincia',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='localidad',
            name='toponim',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='ubicacion',
            name='altitudmax',
            field=models.CharField(max_length=300, null=True, db_column='altitudMax'),
        ),
        migrations.AlterField(
            model_name='ubicacion',
            name='altitudmin',
            field=models.CharField(max_length=300, null=True, db_column='altitudMin'),
        ),
        migrations.AlterField(
            model_name='ubicacion',
            name='cordinate',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='ubicacion',
            name='latitudx',
            field=models.CharField(max_length=300, null=True, db_column='latitudX'),
        ),
        migrations.AlterField(
            model_name='ubicacion',
            name='longitudy',
            field=models.CharField(max_length=300, null=True, db_column='longitudY'),
        ),
        migrations.AlterField(
            model_name='ubicacion',
            name='utmwgs',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
