# Generated by Django 3.1.7 on 2021-05-03 00:41

from django.db import migrations
import django_measurement.models
import measurement.measures.distance
import workout_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_app', '0069_auto_20210502_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutlinked',
            name='dist',
            field=django_measurement.models.MeasurementField(blank=True, measurement=measurement.measures.distance.Distance, validators=[workout_app.models.validate_positive_dist]),
        ),
    ]
