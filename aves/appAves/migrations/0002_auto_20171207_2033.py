# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appAves', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='ave',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='bibliografia',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='endemismo',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='familia',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='migracion',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='ubicacion',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='uicn',
            options={'managed': False},
        ),
    ]
