# Generated by Django 3.2 on 2021-05-06 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hunter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('experience_level', models.IntegerField()),
                ('money', models.IntegerField()),
                ('rank', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('min_size', models.IntegerField()),
                ('max_size', models.IntegerField()),
                ('combat_strategy', models.SmallIntegerField()),
                ('rank', models.SmallIntegerField()),
            ],
            options={
                'verbose_name': 'Monster',
                'verbose_name_plural': 'Monsters',
                'db_table': 'monsters',
            },
        ),
        migrations.CreateModel(
            name='Palico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('experience_level', models.IntegerField()),
                ('combat_style', models.SmallIntegerField()),
                ('rank', models.SmallIntegerField()),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='Monster_Hunter.hunter')),
            ],
        ),
    ]
