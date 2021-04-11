# Generated by Django 3.1.7 on 2021-04-08 02:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workout_app', '0035_achievement'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='achievement',
            name='has_end_date',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='achievement',
            name='has_specific_WorkoutTypeCount',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='achievement',
            name='has_specific_workoutType',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='achievement',
            name='has_start_date',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='achievement',
            name='specific_WorkoutTypeCount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workout_app.workouttypecount'),
        ),
        migrations.AddField(
            model_name='achievement',
            name='specific_WorkoutTypeCount_min',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='achievement',
            name='specific_workoutType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workout_app.workouttype'),
        ),
        migrations.AddField(
            model_name='achievement',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
