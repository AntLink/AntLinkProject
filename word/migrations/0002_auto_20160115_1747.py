# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='cost',
        ),
        migrations.AddField(
            model_name='word',
            name='word_meta',
            field=models.TextField(null=True, blank=True),
        ),
    ]
