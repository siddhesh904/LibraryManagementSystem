# Generated by Django 4.2.1 on 2023-10-01 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_fetchbook_availability_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fetchbook',
            name='average_rating',
            field=models.FloatField(blank=True),
        ),
    ]