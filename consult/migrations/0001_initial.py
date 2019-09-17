# Generated by Django 2.1.7 on 2019-06-29 19:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=5000)),
                ('email', models.CharField(blank=True, max_length=5000)),
                ('phone', models.CharField(blank=True, max_length=5000)),
                ('message', models.TextField(blank=True)),
                ('description1', models.TextField(blank=True)),
                ('description2', models.TextField(blank=True)),
                ('description3', models.TextField(blank=True)),
                ('description4', models.TextField(blank=True)),
                ('description5', models.TextField(blank=True)),
                ('description6', models.TextField(blank=True)),
                ('date_sent', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
