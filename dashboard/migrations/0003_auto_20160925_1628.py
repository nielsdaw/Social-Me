# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 16:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_userprofile_useridfb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='userIdFB',
            new_name='facebook_username',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
