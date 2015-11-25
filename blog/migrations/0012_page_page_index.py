# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_page_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='page_index',
            field=models.IntegerField(default=0),
        ),
    ]
