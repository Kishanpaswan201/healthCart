# Generated by Django 5.0.4 on 2024-04-17 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0002_myuser_first_name_myuser_city_myuser_country_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="myuser",
            old_name="First_name",
            new_name="first_name",
        ),
        migrations.AlterField(
            model_name="myuser",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True),
        ),
    ]
