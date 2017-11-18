# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 23:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ide', '0002_auto_20171021_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussionchannel',
            name='for_all_members',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='discussionmessage',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussion_message_set', to='ide.DiscussionChannel'),
        ),
    ]
