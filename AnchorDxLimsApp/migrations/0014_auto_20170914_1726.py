# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-14 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnchorDxLimsApp', '0013_clinicalsampleinfo_taskprogress'),
    ]

    operations = [
        migrations.CreateModel(
            name='DNAExtractInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('department', models.CharField(max_length=64)),
                ('sam_code_num', models.CharField(max_length=64)),
                ('ExperimentNumber', models.CharField(max_length=64)),
                ('DNA_Concentration', models.CharField(max_length=32)),
                ('DNA_volume', models.CharField(max_length=32)),
                ('DNA_Total', models.CharField(max_length=32)),
                ('Quality_inspection_method', models.CharField(max_length=32)),
                ('Quality_inspection_result', models.CharField(max_length=64)),
                ('Quality_inspection_volume', models.CharField(max_length=32)),
                ('Residual_volume', models.CharField(max_length=32)),
                ('Extraction_kit_type', models.CharField(max_length=128)),
                ('DNA_extraction_people', models.CharField(max_length=32)),
                ('DNA_extraction_time', models.CharField(max_length=32)),
                ('DNA_extraction_remarks', models.CharField(max_length=512)),
                ('DNA_extraction_review_people', models.CharField(max_length=64)),
                ('DNA_extraction_review_Time', models.CharField(max_length=32)),
                ('DNA_extraction_review_Remarks', models.CharField(max_length=512)),
            ],
        ),
        migrations.DeleteModel(
            name='clinicalSampleInfo_Not_Pass',
        ),
        migrations.DeleteModel(
            name='clinicalSampleInfo_Pass',
        ),
    ]