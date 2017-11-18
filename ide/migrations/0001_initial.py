# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 13:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commited_on', models.DateTimeField()),
                ('state', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='DiscussionChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='DiscussionMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('time', models.DateTimeField()),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ide.DiscussionChannel')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('token', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.IntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ide.Project')),
            ],
        ),
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admins', to='ide.SiteUser'),
        ),
        migrations.AddField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(to='ide.SiteUser'),
        ),
        migrations.AddField(
            model_name='discussionmessage',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ide.SiteUser'),
        ),
        migrations.AddField(
            model_name='discussionchannel',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ide.Project'),
        ),
        migrations.AddField(
            model_name='commit',
            name='commited_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ide.SiteUser'),
        ),
        migrations.AddField(
            model_name='commit',
            name='repo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ide.Repo'),
        ),
    ]
