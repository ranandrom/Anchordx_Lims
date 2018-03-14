# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-12-25 03:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnchorDxLimsApp', '0057_auto_20171222_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='RandDSampleComputerSeqInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('department', models.CharField(max_length=64)),
                ('sam_code_num', models.CharField(max_length=64)),
                ('PreLibConName', models.CharField(max_length=64)),
                ('FinLibConName', models.CharField(max_length=32)),
                ('DNA_Concentration', models.CharField(max_length=32)),
                ('DilutionMultiple', models.CharField(max_length=16)),
                ('qPCR', models.CharField(max_length=16)),
                ('AverageLengthLibrary', models.CharField(max_length=32)),
                ('LibEffConcentration', models.CharField(max_length=32)),
                ('QuantitativeTime', models.CharField(max_length=32)),
                ('FinLibCon_storage_location', models.CharField(max_length=32)),
                ('QuantitativeHuman', models.CharField(max_length=32)),
                ('SeqRemarks', models.CharField(max_length=512)),
                ('DataPath', models.CharField(max_length=64)),
                ('Next_TaskProgress_Man', models.CharField(max_length=64)),
                ('Next_TaskProgress_Time', models.CharField(max_length=32)),
                ('Next_TaskProgress_Remarks', models.CharField(max_length=512)),
                ('Next_TaskProgress_Sign', models.CharField(max_length=16)),
                ('DNA_extraction_num', models.CharField(max_length=16)),
                ('Build_Prelib_num', models.CharField(max_length=16)),
                ('Build_finlib_num', models.CharField(max_length=16)),
                ('ExperimentTimes', models.CharField(max_length=16)),
                ('Bioinfo_Sign', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='RandDSampleFinLibConInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('department', models.CharField(max_length=64)),
                ('sam_code_num', models.CharField(max_length=64)),
                ('PreLibConName', models.CharField(max_length=64)),
                ('PoolInternalLibNumber', models.CharField(max_length=32)),
                ('FinLibConName', models.CharField(max_length=32)),
                ('DNA_Concentration', models.CharField(max_length=32)),
                ('DNA_volume', models.CharField(max_length=32)),
                ('DNA_Total', models.CharField(max_length=32)),
                ('Indexi5i7', models.CharField(max_length=32)),
                ('Panel', models.CharField(max_length=32)),
                ('Build_lib_time', models.CharField(max_length=32)),
                ('FinLibCon_storage_location', models.CharField(max_length=32)),
                ('Build_lib_man', models.CharField(max_length=32)),
                ('SequencingInfo', models.CharField(max_length=64)),
                ('Build_lib_remarks', models.CharField(max_length=512)),
                ('Next_TaskProgress', models.CharField(max_length=64)),
                ('Next_TaskProgress_Man', models.CharField(max_length=64)),
                ('Next_TaskProgress_Time', models.CharField(max_length=32)),
                ('Next_TaskProgress_Remarks', models.CharField(max_length=512)),
                ('Next_TaskProgress_Sign', models.CharField(max_length=16)),
                ('DNA_extraction_num', models.CharField(max_length=16)),
                ('Build_Prelib_num', models.CharField(max_length=16)),
                ('ExperimentTimes', models.CharField(max_length=16)),
                ('ComputerSeq_Sign', models.CharField(max_length=16)),
            ],
        ),
        migrations.RenameField(
            model_name='randdsampleprelibconinfo',
            old_name='Concentration',
            new_name='DNA_Concentration',
        ),
    ]
