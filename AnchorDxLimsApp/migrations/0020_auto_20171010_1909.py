# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-10 11:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AnchorDxLimsApp', '0019_prelibconinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prelibconinfo',
            old_name='Extraction_kit_type',
            new_name='Build_lib_method',
        ),
    ]
