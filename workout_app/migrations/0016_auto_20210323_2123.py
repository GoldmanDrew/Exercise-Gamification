# Generated by Django 3.1.7 on 2021-03-24 01:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_app', '0015_auto_20210323_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutlinked',
            name='end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='workoutlinked',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
