# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('account', models.CharField(max_length=16, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
    ]
