# Generated by Django 4.1.3 on 2022-11-27 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0020_lesson_lesson_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='lesson_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lessonrequest'),
        ),
    ]