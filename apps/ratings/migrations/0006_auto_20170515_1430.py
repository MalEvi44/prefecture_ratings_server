# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-15 14:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0005_auto_20170515_1425'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='monthlyratingsubelement',
            options={'ordering': ('name',), 'verbose_name': 'Подкомпонент месячного рейтинга', 'verbose_name_plural': 'Подкомпоненты месячных рейтингов'},
        ),
    ]
