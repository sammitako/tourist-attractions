# Generated by Django 2.2.5 on 2021-02-14 08:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0005_auto_20210210_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_rate',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
