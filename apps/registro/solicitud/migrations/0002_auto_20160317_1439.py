# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registros',
            name='codigo_centro',
            field=models.IntegerField(max_length=25, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='registros',
            name='nombre_centro',
            field=models.CharField(max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
    ]
