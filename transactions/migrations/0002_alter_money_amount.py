# Generated by Django 4.2 on 2023-04-27 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="money", name="amount", field=models.IntegerField(),
        ),
    ]
