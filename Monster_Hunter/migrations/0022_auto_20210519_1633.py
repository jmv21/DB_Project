# Generated by Django 3.2 on 2021-05-19 20:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monster_Hunter', '0021_auto_20210519_1537'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collected_object',
            options={'verbose_name_plural': 'Collected Objects'},
        ),
        migrations.AlterModelOptions(
            name='merchantable_object',
            options={'verbose_name': 'Merchantable Object', 'verbose_name_plural': 'Merchantable Objects'},
        ),
        migrations.AlterField(
            model_name='armor',
            name='armor_type',
            field=models.SmallIntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
        migrations.AlterField(
            model_name='elemental_defense',
            name='value',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='monster',
            name='combat_strategy',
            field=models.TextField(default='No strategy'),
        ),
        migrations.AlterField(
            model_name='monster',
            name='max_size',
            field=models.PositiveIntegerField(default=10, validators=[django.core.validators.MinValueValidator(2)]),
        ),
        migrations.AlterField(
            model_name='monster',
            name='min_size',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='monster',
            name='rank',
            field=models.SmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)]),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='damage',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='weapon_type',
            field=models.SmallIntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
    ]
