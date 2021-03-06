# Generated by Django 3.2 on 2021-05-06 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Monster_Hunter', '0003_auto_20210506_0333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weapon_type', models.CharField(max_length=80)),
                ('damage', models.IntegerField(default=5)),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Monster_Hunter.object')),
            ],
        ),
        migrations.CreateModel(
            name='Merchantable_Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.TextField()),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Monster_Hunter.object')),
            ],
        ),
        migrations.CreateModel(
            name='Collected_object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(default='Astera', max_length=80)),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Monster_Hunter.object')),
            ],
        ),
        migrations.CreateModel(
            name='Armor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('armor_type', models.SmallIntegerField()),
                ('defense', models.IntegerField(default=5)),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Monster_Hunter.object')),
            ],
        ),
    ]
