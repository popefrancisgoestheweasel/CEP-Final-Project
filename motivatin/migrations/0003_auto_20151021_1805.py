# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('motivatin', '0002_auto_20151021_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='booleanchain',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
