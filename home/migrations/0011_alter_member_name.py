# Generated by Django 4.2.5 on 2023-10-01 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_fetchbook_average_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
