# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-04-22 09:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pinax_messages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollabMessage',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('pinax_messages.message',),
        ),
        migrations.CreateModel(
            name='CollabThread',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('pinax_messages.thread',),
        ),
    ]
