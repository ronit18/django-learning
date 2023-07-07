# Generated by Django 4.2.3 on 2023-07-07 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("student", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subject",
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
                ("subject_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="SubjectMarks",
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
                ("marks", models.IntegerField(default=0)),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="student",
                        to="student.student",
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subject",
                        to="student.subject",
                    ),
                ),
            ],
            options={
                "unique_together": {("student", "subject")},
            },
        ),
    ]