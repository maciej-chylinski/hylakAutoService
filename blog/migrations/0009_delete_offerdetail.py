# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180212_1550'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OfferDetail',
        ),
    ]
