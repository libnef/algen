# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 12:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0003_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.Problem')),
            ],
        ),
    ]
