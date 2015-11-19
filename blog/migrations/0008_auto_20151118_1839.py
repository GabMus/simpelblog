# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20151118_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='post_ptr',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
