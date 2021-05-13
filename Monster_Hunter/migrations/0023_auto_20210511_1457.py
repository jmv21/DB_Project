# Generated by Django 3.2 on 2021-05-11 18:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Monster_Hunter', '0022_auto_20210519_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='min_size',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='object1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Monster_Hunter.object'),
        ),
    ]