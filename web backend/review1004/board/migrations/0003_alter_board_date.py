# Generated by Django 4.1.1 on 2022-10-04 01:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_alter_board_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
