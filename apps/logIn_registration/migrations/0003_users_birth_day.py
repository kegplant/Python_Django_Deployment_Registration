# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-20 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logIn_registration', '0002_users_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='birth_day',
            field=models.DateField(default='2007-10-11'),
        ),
    ]