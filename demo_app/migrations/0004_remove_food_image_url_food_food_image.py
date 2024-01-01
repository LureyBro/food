# Generated by Django 4.2.2 on 2023-07-10 11:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("demo_app", "0003_food_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="food",
            name="image_url",
        ),
        migrations.AddField(
            model_name="food",
            name="Food_image",
            field=models.FileField(null=True, upload_to="static/uploads"),
        ),
    ]