# Generated by Django 5.0.2 on 2024-03-21 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diets', '0009_remove_mealtoclient_meal_time_meal_meal_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='food_id',
            field=models.IntegerField(null=True),
        ),
    ]