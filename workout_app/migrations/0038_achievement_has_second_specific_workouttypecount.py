# Generated by Django 3.1.7 on 2021-04-08 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_app', '0037_auto_20210407_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='has_second_specific_WorkoutTypeCount',
            field=models.BooleanField(default=False),
        ),
    ]
