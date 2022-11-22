# Generated by Django 4.1.3 on 2022-11-22 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lessons", "0003_user_is_student"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_student",
        ),
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(default="Student", max_length=255),
        ),
    ]