# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-01-10 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnchorDxLimsApp', '0065_remove_randdsampleinfo_reviewer'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinicalsampleinfo',
            name='TissueSampleSign',
            field=models.CharField(default=0, max_length=16),
            preserve_default=False,
        ),
    ]
