# Generated by Django 5.0.2 on 2024-02-22 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='ingredients',
            field=models.JSONField(null=True),
        ),
    ]