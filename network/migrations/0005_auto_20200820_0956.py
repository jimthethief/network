# Generated by Django 3.0.8 on 2020-08-20 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_auto_20200820_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='edited',
            field=models.DateTimeField(blank=True, default=None),
        ),
    ]
