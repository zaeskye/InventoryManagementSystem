# Generated by Django 5.0.1 on 2024-01-04 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplierid', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('suppliername', models.TextField()),
            ],
        ),
    ]
