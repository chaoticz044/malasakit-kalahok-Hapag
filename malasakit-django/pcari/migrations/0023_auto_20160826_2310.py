# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-26 23:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcari', '0022_quantitativequestion_average_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='tagalog_comment',
            field=models.CharField(default='', max_length=1000, null=True),
        ),
    ]
