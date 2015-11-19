# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_posttitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='piclink',
            field=models.TextField(blank=True),
        ),
    ]
