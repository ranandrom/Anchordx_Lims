# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-03-06 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnchorDxLimsApp', '0076_auto_20180205_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='computerseqinfo',
            name='ReviewResult',
            field=models.CharField(default=0, max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='randdsamplecomputerseqinfo',
            name='ReviewResult',
            field=models.CharField(default=0, max_length=16),
            preserve_default=False,
        ),
    ]