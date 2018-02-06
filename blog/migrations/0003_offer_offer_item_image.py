# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='offer_item_image',
            field=models.ImageField(default='static/img/empty_offer_item.jpg', upload_to=blog.models.offer_item_upload_path),
        ),
    ]
