# Generated by Django 5.0.1 on 2024-01-09 03:09

import django.db.models.functions.datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_stock_stockstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='stockstatus',
            field=models.CharField(default=django.db.models.functions.datetime.Now, max_length=5),
        ),
    ]
