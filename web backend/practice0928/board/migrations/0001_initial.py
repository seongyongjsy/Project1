# Generated by Django 4.1.1 on 2022-09-28 05:08

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
                ('num', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('writer', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 9, 28, 14, 8, 19, 948656))),
            ],
        ),
    ]
