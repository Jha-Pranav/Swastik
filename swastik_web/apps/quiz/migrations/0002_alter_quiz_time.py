# Generated by Django 4.2 on 2023-06-03 17:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quiz", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quiz",
            name="time",
            field=models.IntegerField(
                default="1800", help_text="Duration of the quiz in seconds"
            ),
        ),
    ]
