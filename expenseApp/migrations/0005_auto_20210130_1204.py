# Generated by Django 3.1.5 on 2021-01-30 12:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenseApp', '0004_auto_20210130_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2021, 1, 30)),
        ),
    ]
