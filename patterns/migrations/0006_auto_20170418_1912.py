# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-18 19:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patterns', '0005_auto_20170418_1911'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pattern',
            old_name='gist',
            new_name='gists',
        ),
    ]
