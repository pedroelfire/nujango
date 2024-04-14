# Generated by Django 5.0.2 on 2024-02-24 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diets', '0002_alter_meal_ingredients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_id', models.JSONField(null=True)),
                ('metric_serving_unit', models.CharField(choices=[('g', 'grams'), ('ml', 'milliliters'), ('tbsp', 'tablespoons')], max_length=4)),
                ('metric_serving_amount', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='meal',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='meal',
            name='ingredients',
            field=models.ManyToManyField(to='diets.ingredients'),
        ),
    ]