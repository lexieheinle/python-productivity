# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('name_slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Lake',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('name_slug', models.SlugField()),
                ('site_id', models.CharField(max_length=3)),
                ('county', models.ForeignKey(to='reports.County')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('alert', models.BooleanField()),
                ('toxin', models.FloatField()),
                ('ecoli', models.IntegerField()),
                ('lake', models.ForeignKey(to='reports.Lake')),
            ],
        ),
    ]
