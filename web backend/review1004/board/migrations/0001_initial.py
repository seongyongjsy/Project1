# Generated by Django 4.1.1 on 2022-10-04 01:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('num', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('writer', models.CharField(max_length=20)),
                ('content', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 10, 4, 10, 9, 47, 512937))),
            ],
        ),
    ]
