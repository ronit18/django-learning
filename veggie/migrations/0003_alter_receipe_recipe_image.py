# Generated by Django 4.2.3 on 2023-07-06 17:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "veggie",
            "0002_rename_reciepe_description_receipe_recipe_description_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="receipe",
            name="recipe_image",
            field=models.ImageField(upload_to="recipe"),
        ),
    ]
