# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-01-12 06:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AnchorDxLimsApp', '0071_bioinfodataanalysisinfo_samplesource'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bioinfodataanalysisinfo',
            name='SampleSource',
        ),
    ]