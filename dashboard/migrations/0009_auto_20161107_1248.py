# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20160926_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_id', models.IntegerField(default=0)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('facebook_email', models.EmailField(default='', max_length=254)),
                ('gender', models.CharField(max_length=20)),
                ('profile_picture_url', models.TextField(default='')),
                ('friends_count', models.IntegerField(default=0)),
                ('link', models.TextField(default='')),
                ('age_range', models.IntegerField(default=0)),
                ('last_updated', models.DateTimeField(default='')),
                ('auth_token', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='GoogleProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='InstagramProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram_id', models.IntegerField(default=0)),
                ('profile_picture_url', models.TextField(default='')),
                ('bio', models.TextField(default='')),
                ('website', models.CharField(default='', max_length=100)),
                ('username', models.CharField(default='', max_length=255)),
                ('full_name', models.CharField(default='', max_length=255)),
                ('access_token', models.TextField(default='')),
                ('number_of_followers', models.IntegerField(default=0)),
                ('number_of_pictures', models.IntegerField(default=0)),
                ('number_of_following', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='LinkedinProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=255)),
                ('last_name', models.CharField(default='', max_length=255)),
                ('email', models.EmailField(default='', max_length=254)),
                ('headline', models.TextField(default='')),
                ('industry', models.TextField(default='')),
                ('location', models.TextField(default='')),
                ('recent_shared', models.TextField(default='')),
                ('number_of_connections', models.IntegerField(default=0)),
                ('summary', models.TextField(default='')),
                ('specialities', models.TextField(default='')),
                ('current_position', models.TextField(default='')),
                ('profile_picture_url', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='SoundCloudProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SpotifyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TwitterProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]