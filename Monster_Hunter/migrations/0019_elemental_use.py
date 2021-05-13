# Generated by Django 3.2 on 2021-05-18 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Monster_Hunter', '0018_auto_20210518_0123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Elemental_use',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Monster_Hunter.element')),
                ('monster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Monster_Hunter.monster')),
            ],
            options={
                'ordering': ['monster'],
                'unique_together': {('monster', 'element')},
            },
        ),
    ]