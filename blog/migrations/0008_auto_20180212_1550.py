# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_offerdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='id',
            field=models.IntegerField(primary_key=True, unique=True, serialize=False),
        ),
    ]
