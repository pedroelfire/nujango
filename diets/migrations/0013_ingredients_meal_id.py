# Generated by Django 5.0.2 on 2024-03-21 19:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diets', '0012_remove_ingredients_meal_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredients',
            name='meal_id',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='diets.meal'),
        ),
    ]