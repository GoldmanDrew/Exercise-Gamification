# Generated by Django 3.1.7 on 2021-04-05 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_app', '0030_auto_20210405_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workouttype',
            name='has_duration',
            field=models.BooleanField(default=False),
        ),
    ]