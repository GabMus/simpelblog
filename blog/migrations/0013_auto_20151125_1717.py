# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_page_page_index'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='url',
        ),
        migrations.RemoveField(
            model_name='pagepost',
            name='tag',
        ),
        migrations.AlterField(
            model_name='page',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
