# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-08-22 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_checklist', '0004_auto_20180809_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='doctor2',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Второй хирург'),
        ),
    ]
