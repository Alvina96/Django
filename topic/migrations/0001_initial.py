# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='topic_images')),
                ('precedency', models.IntegerField(default=0)),
                ('level', models.IntegerField(default=0)),
                ('parent_id', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]
