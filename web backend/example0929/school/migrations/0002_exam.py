# Generated by Django 4.1.1 on 2022-09-29 02:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=10)),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 9, 29, 11, 8, 34, 668261))),
            ],
        ),
    ]
