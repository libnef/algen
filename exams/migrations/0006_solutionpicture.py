# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 14:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0005_auto_20170411_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolutionPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.Problem')),
            ],
        ),
    ]