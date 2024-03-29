# Generated by Django 4.1.7 on 2023-11-25 18:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("django_app", "0008_alter_news_user_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="news",
            name="id",
        ),
        migrations.AlterField(
            model_name="news",
            name="user_id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
