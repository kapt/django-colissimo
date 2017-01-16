# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colissimo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommanded',
            name='price',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
    ]
