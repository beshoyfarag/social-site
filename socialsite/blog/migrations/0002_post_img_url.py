# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-22 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img_url',
            field=models.URLField(default='https://media.licdn.com/mpr/mpr/shrinknp_200_200/AAEAAQAAAAAAAAtcAAAAJDAyZTQyMjM2LTNiYTUtNDNmMS1iMDRkLTVhM2EyNTU1ZmMxNg.jpg'),
            preserve_default=False,
        ),
    ]