# Generated by Django 4.1.7 on 2023-11-25 18:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_app", "0009_remove_news_id_alter_news_user_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="id",
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]
