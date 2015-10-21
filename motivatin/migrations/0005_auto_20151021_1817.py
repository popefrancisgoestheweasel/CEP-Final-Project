# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('motivatin', '0004_auto_20151021_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='okayokay',
            field=models.TextField(default=b'okayokay'),
            preserve_default=True,
        ),
    ]
