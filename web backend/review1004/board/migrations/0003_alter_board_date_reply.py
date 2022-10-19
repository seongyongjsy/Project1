# Generated by Django 4.1.1 on 2022-10-04 02:27

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_alter_board_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 4, 11, 27, 46, 193828)),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('writer', models.CharField(max_length=20)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.board')),
            ],
        ),
    ]
