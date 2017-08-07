# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-03 08:27
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('understand_question', models.CharField(blank=True, max_length=200, null=True)),
                ('understand_image', models.CharField(blank=True, max_length=200, null=True)),
                ('fluency', models.CharField(blank=True, max_length=200, null=True)),
                ('detail', models.CharField(blank=True, max_length=200, null=True)),
                ('accurate', models.CharField(blank=True, max_length=200, null=True)),
                ('consistent', models.CharField(blank=True, max_length=200, null=True)),
                ('comments', models.CharField(blank=True, max_length=200, null=True)),
                ('worker_id', models.CharField(blank=True, max_length=100, null=True)),
                ('assignment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('level', models.CharField(blank=True, max_length=100, null=True)),
                ('hit_id', models.CharField(blank=True, max_length=100, null=True)),
                ('game_id', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bot', models.CharField(blank=True, max_length=100, null=True)),
                ('is_active', models.NullBooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='GameRound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('socket_id', models.CharField(blank=True, max_length=100, null=True)),
                ('worker_id', models.CharField(blank=True, max_length=100, null=True)),
                ('assignment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('level', models.CharField(blank=True, max_length=100, null=True)),
                ('hit_id', models.CharField(blank=True, max_length=100, null=True)),
                ('game_id', models.CharField(blank=True, max_length=100, null=True)),
                ('round_id', models.CharField(blank=True, max_length=100, null=True)),
                ('question', models.CharField(blank=True, max_length=100, null=True)),
                ('answer', models.CharField(blank=True, max_length=100, null=True)),
                ('history', models.CharField(blank=True, max_length=10000, null=True)),
                ('target_image', models.CharField(blank=True, max_length=100, null=True)),
                ('bot', models.CharField(blank=True, max_length=100, null=True)),
                ('user_picked_image', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.NullBooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImagePool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pool_id', models.CharField(blank=True, max_length=200, null=True)),
                ('caption', models.CharField(blank=True, max_length=1000, null=True)),
                ('easy_pool', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('medium_pool', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('hard_pool', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('obj', models.CharField(blank=True, max_length=200, null=True)),
                ('target_image', models.CharField(blank=True, max_length=200, null=True)),
                ('is_active', models.NullBooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ImageRanking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('socket_id', models.CharField(blank=True, max_length=100, null=True)),
                ('worker_id', models.CharField(blank=True, max_length=100, null=True)),
                ('assignment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('level', models.CharField(blank=True, max_length=100, null=True)),
                ('hit_id', models.CharField(blank=True, max_length=100, null=True)),
                ('game_id', models.CharField(blank=True, max_length=100, null=True)),
                ('target_image', models.CharField(blank=True, max_length=100, null=True)),
                ('final_image_list', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bot', models.CharField(blank=True, max_length=100, null=True)),
                ('score', models.FloatField(default=0)),
                ('is_active', models.NullBooleanField(default=True)),
            ],
        ),
    ]