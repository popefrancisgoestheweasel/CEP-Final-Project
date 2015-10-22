# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('motivatin', '0005_auto_20151021_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='chainminusone',
            field=models.IntegerField(default=-1),
            preserve_default=True,
        ),
    ]
