# Generated by Django 5.0.2 on 2024-03-21 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diets', '0013_ingredients_meal_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailymeal',
            name='meals',
            field=models.ManyToManyField(null=True, to='diets.meal'),
        ),
    ]
