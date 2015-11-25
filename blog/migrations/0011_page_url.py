# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20151125_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='url',
            field=models.TextField(default='/'),
        ),
    ]
