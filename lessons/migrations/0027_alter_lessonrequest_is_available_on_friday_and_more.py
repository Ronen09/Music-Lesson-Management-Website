# Generated by Django 4.1.3 on 2022-12-08 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0026_alter_lessonrequest_is_available_on_friday_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonrequest',
            name='is_available_on_friday',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='lessonrequest',
            name='is_available_on_monday',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='lessonrequest',
            name='is_available_on_thursday',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='lessonrequest',
            name='is_available_on_tuesday',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='lessonrequest',
            name='is_available_on_wednesday',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
