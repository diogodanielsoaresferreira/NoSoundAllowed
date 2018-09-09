# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-17 12:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ValuesReceived',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('timestamp', models.DateTimeField()),
                ('value_type', models.CharField(choices=[('NO', 'Noise'), ('TE', 'Temperature'), ('LE', 'Led')], max_length=2, unique=True)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Sensor')),
            ],
        ),
    ]
