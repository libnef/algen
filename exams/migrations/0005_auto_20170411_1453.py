# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 12:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0004_tag'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('problem', 'tag')]),
        ),
    ]
