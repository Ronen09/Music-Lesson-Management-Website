# Generated by Django 4.1.3 on 2022-11-26 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0015_term_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='order',
            field=models.IntegerField(),
        ),
    ]