# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('motivatin', '0003_auto_20151021_1805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='booleanchain',
            new_name='okayokay',
        ),
    ]
