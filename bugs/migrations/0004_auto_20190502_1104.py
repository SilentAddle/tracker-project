# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-02 11:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0003_auto_20190502_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugs',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
