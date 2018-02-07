# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180207_1035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('contact_title', models.CharField(max_length=100)),
                ('contact_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
