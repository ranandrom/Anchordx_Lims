# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-02 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnchorDxLimsApp', '0003_clinicalsampleinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinicalsampleinfo',
            name='product_name',
            field=models.CharField(max_length=128),
        ),
    ]