# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 14:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=6)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(default='', max_length=1)),
                ('problem', models.CharField(default='', max_length=2)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.Exam')),
            ],
        ),
    ]
