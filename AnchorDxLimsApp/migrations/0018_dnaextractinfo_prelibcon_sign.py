# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-10 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnchorDxLimsApp', '0017_dnaextractinfo_taskprogress'),
    ]

    operations = [
        migrations.AddField(
            model_name='dnaextractinfo',
            name='PreLibCon_Sign',
            field=models.CharField(default='0', max_length=16),
            preserve_default=False,
        ),
    ]