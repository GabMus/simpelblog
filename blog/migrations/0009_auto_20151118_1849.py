# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20151118_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('posttitle', models.TextField(default='Post')),
                ('post', models.TextField()),
                ('piclink', models.TextField(blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('article_ptr', models.OneToOneField(to='blog.Article', serialize=False, auto_created=True, parent_link=True, primary_key=True)),
            ],
            bases=('blog.article',),
        ),
        migrations.CreateModel(
            name='PagePost',
            fields=[
                ('article_ptr', models.OneToOneField(to='blog.Article', serialize=False, auto_created=True, parent_link=True, primary_key=True)),
                ('tag', models.CharField(default='default', max_length=150)),
            ],
            bases=('blog.article',),
        ),
    ]
