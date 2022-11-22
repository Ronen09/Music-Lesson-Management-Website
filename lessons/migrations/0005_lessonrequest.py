# Generated by Django 4.1.3 on 2022-11-22 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lessons", "0004_remove_user_is_student_user_role"),
    ]

    operations = [
        migrations.CreateModel(
            name="LessonRequest",
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
                ("is_available_on_monday", models.BooleanField()),
                ("is_available_on_tuesday", models.BooleanField()),
                ("is_available_on_wednesday", models.BooleanField()),
                ("is_available_on_thursday", models.BooleanField()),
                ("is_available_on_friday", models.BooleanField()),
                ("no_of_lessons", models.IntegerField()),
                ("lesson_interval_in_days", models.IntegerField()),
                ("lesson_duration_in_mins", models.IntegerField()),
                ("further_information", models.CharField(max_length=255)),
            ],
        ),
    ]
