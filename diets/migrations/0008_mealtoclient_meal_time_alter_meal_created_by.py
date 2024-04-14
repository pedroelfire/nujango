# Generated by Django 5.0.2 on 2024-03-07 01:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('diets', '0007_meal_mealtoclient'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealtoclient',
            name='meal_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='created_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='client.nutritionist'),
        ),
    ]