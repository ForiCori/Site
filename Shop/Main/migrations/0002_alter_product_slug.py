# Generated by Django 5.1.4 on 2024-12-22 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True, verbose_name='Slug'),
        ),
    ]
