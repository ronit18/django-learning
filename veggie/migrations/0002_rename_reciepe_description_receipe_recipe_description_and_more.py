# Generated by Django 4.2.3 on 2023-07-06 17:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("veggie", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="receipe",
            old_name="reciepe_description",
            new_name="recipe_description",
        ),
        migrations.RenameField(
            model_name="receipe",
            old_name="reciepe_image",
            new_name="recipe_image",
        ),
        migrations.RenameField(
            model_name="receipe",
            old_name="reciepe_name",
            new_name="recipe_name",
        ),
    ]
