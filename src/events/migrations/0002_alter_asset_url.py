# Generated by Django 4.1.7 on 2023-04-01 22:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="asset",
            name="url",
            field=models.FileField(upload_to="assets/"),
        ),
    ]
