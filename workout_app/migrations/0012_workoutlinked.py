# Generated by Django 3.1.7 on 2021-03-24 00:37

from django.db import migrations, models
import django.db.models.deletion
import django_measurement.models
import measurement.measures.distance


class Migration(migrations.Migration):

    dependencies = [
        ('workout_app', '0011_workouttype_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutLinked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dist', django_measurement.models.MeasurementField(measurement=measurement.measures.distance.Distance)),
                ('workoutType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workout_app.workouttype')),
            ],
        ),
    ]