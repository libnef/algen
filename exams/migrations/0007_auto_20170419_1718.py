# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0006_solutionpicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solutionpicture',
            name='picture',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='exams/static/home_solutions/'),
        ),
    ]