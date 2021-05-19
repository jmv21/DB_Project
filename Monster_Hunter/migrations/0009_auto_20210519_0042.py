# Generated by Django 3.2 on 2021-05-19 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Monster_Hunter', '0008_auto_20210519_0039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipes',
            name='name',
        ),
        migrations.AlterField(
            model_name='recipes',
            name='object2',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='object2', to='Monster_Hunter.object'),
        ),
    ]