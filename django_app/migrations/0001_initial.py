# Generated by Django 4.1.7 on 2023-11-25 14:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "user_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("news_api", models.CharField(max_length=200)),
                ("news_file", models.CharField(max_length=200)),
                ("news_providers", models.CharField(max_length=200)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-updated", "-created"],
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "user_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("userName", models.CharField(max_length=200, unique=True)),
                ("userPassword", models.CharField(max_length=200, unique=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-updated", "-created"],
            },
        ),
        migrations.CreateModel(
            name="Weather",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("weather_api", models.CharField(max_length=200)),
                ("weather_city", models.CharField(max_length=200)),
                ("weather_country", models.CharField(max_length=200)),
                ("weather_longitude", models.CharField(max_length=200)),
                ("weather_latitude", models.CharField(max_length=200)),
                ("use_coordinates", models.BooleanField(default=False)),
                ("weather_file", models.CharField(max_length=200)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-updated", "-created"],
            },
        ),
    ]