# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acs_app', '0002_auto_20170414_0052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passtypes',
            name='title',
        ),
        migrations.AddField(
            model_name='passtypes',
            name='pass_type',
            field=models.CharField(choices=[('enter', 'Вход'), ('exit', 'Выход')], max_length=2, null=True),
        ),
    ]
