# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-01-15 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnchorDxLimsApp', '0074_bioinfodataanalysisinfo_samplesource'),
    ]

    operations = [
        migrations.AddField(
            model_name='bioinfodataanalysisinfo',
            name='GeneticCounselor',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bioinfodataanalysisinfo',
            name='Operater',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bioinfodataanalysisinfo',
            name='Report_Send_Man',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
    ]
