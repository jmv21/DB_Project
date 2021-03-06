# Generated by Django 3.2 on 2021-05-31 22:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monster_Hunter', '0023_auto_20210511_1457'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='elemental_defense',
            options={},
        ),
        migrations.AlterField(
            model_name='palico',
            name='combat_style',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='palico',
            name='experience_level',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='palico',
            name='rank',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)]),
        ),
        migrations.AlterUniqueTogether(
            name='elemental_defense',
            unique_together=set(),
        ),
    ]
