# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-18 14:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0006_auto_20170515_1430'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='monthlyratingsubelement',
            options={'ordering': ('id',), 'verbose_name': 'Подкомпонент месячного рейтинга', 'verbose_name_plural': 'Подкомпоненты месячных рейтингов'},
        ),
    ]
