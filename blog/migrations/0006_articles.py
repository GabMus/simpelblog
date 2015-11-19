# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('post_ptr', models.OneToOneField(to='blog.Post', parent_link=True, primary_key=True, serialize=False, auto_created=True)),
                ('tag', models.CharField(default='gear', max_length=150)),
            ],
            bases=('blog.post',),
        ),
    ]
