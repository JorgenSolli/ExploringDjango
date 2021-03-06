# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 10:50
from __future__ import unicode_literals

import booking.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20170322_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='hotel_id',
        ),
        migrations.AddField(
            model_name='reservation',
            name='hotel',
            field=models.IntegerField(default=0, verbose_name=booking.models.Hotel),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='hotel',
            unique_together=set([('name', 'city')]),
        ),
    ]
