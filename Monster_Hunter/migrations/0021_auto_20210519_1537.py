# Generated by Django 3.2 on 2021-05-19 19:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monster_Hunter', '0020_alter_armor_defense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armor',
            name='armor_type',
            field=models.SmallIntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
        migrations.AlterField(
            model_name='armor',
            name='defense',
            field=models.PositiveIntegerField(default=5, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='hunter',
            name='experience_level',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='hunter',
            name='money',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='hunter',
            name='rank',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='quantity',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(999)]),
        ),
        migrations.AlterField(
            model_name='merchantable_object',
            name='price',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='quantity',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(999)]),
        ),
    ]
