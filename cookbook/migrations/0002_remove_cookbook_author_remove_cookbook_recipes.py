# Generated by Django 5.0.3 on 2024-03-20 11:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cookbook", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cookbook",
            name="author",
        ),
        migrations.RemoveField(
            model_name="cookbook",
            name="recipes",
        ),
    ]