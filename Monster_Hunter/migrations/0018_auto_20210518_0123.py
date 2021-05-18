# Generated by Django 3.2 on 2021-05-18 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monster_Hunter', '0017_auto_20210518_0122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reward_object',
            options={'ordering': ['monster_id']},
        ),
        migrations.AlterUniqueTogether(
            name='reward_object',
            unique_together={('object_id', 'monster_id')},
        ),
    ]
