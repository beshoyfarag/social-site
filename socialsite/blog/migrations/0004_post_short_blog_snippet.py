# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-22 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20171122_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='short_blog_snippet',
            field=models.CharField(default='mysnippet man', max_length=15),
            preserve_default=False,
        ),
    ]
