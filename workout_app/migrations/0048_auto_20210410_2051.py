# Generated by Django 3.1.7 on 2021-04-11 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout_app', '0047_auto_20210410_2030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='achievement',
            old_name='pace_per_mile',
            new_name='max_pace_per_mile',
        ),
    ]
