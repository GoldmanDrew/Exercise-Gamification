# Generated by Django 3.1.7 on 2021-03-24 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout_app', '0027_workoutlinked_one_day'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Workout',
        ),
    ]