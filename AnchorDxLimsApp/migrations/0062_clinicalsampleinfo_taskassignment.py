# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-01-04 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnchorDxLimsApp', '0061_auto_20180104_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinicalsampleinfo',
            name='TaskAssignment',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
    ]