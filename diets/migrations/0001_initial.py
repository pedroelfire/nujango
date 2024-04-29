# Generated by Django 3.2.25 on 2024-04-24 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='client.nutritionist')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_id', models.IntegerField(null=True)),
                ('metric_serving_unit', models.CharField(choices=[('g', 'grams'), ('ml', 'milliliters'), ('tbsp', 'tablespoons')], max_length=4)),
                ('metric_serving_amount', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='MealToClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='client.client')),
                ('diet', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='diets.diet')),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('meal_time', models.TimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='client.nutritionist')),
                ('ingredients', models.ManyToManyField(blank=True, default=0, to='diets.Ingredients')),
            ],
        ),
        migrations.AddField(
            model_name='diet',
            name='meals',
            field=models.ManyToManyField(blank=True, to='diets.Meal'),
        ),
    ]
