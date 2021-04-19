from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django_measurement.models import MeasurementField
from measurement.measures import Distance, Weight

# from django.conf import settings
import datetime

from pathlib import Path
import os

# Create your models here.

# class Workout(models.Model):
#     type = models.CharField(max_length=30, default='', blank=True)
#     duration = models.CharField(max_length=30, default='', blank=True)
#     intensity = models.CharField(max_length=30, default='', blank=True)
#     steps = models.CharField(max_length=30, default='', blank=True)
#     miles = models.CharField(max_length=30, default='', blank=True)
#     profile = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return "type: " + self.type
#     def get_absolute_url(self):
#         return reverse('workout_list')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    achievement_points = models.PositiveIntegerField(default = 0)
    achievement_num = models.PositiveIntegerField(default = 0)
    zipcode = models.CharField(max_length=5, default='22904')
    def __str__(self):
        return str(self.user)

class WorkoutTypeCount(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    type_name = models.CharField(max_length=30, default='')
    def __str__(self):
        return self.type_name

class WorkoutType(models.Model):
    type_name = models.CharField(max_length=30, default='')
    has_intensity = models.BooleanField(default=False)
    has_duration = models.BooleanField(default=False)
    has_distance_comp = models.BooleanField(default=False)
    has_first_count_component = models.BooleanField(default=False)
    first_count_component = models.ForeignKey(WorkoutTypeCount, on_delete=models.CASCADE, null=True, blank=True)
    has_second_count_component = models.BooleanField(default=False)
    second_count_component = models.ForeignKey(WorkoutTypeCount, on_delete=models.CASCADE, related_name='second_cc', null=True, blank=True)
    has_set_rep_comp = models.BooleanField(default=False)
    has_weight_comp = models.BooleanField(default=False)
    is_official_type = models.BooleanField(default=False)
    profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.type_name

INTENSITY_CHOICES = (
    ('L', 'Light'),
    ('M', 'Moderate'),
    ('V', 'Vigorous'),
    ('NA', 'Not Applicable')
)


class WorkoutLinked(models.Model):
    workoutType = models.ForeignKey(WorkoutType, on_delete=models.CASCADE)
    profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    zipcode = models.CharField(max_length=5, default='22904')
    start_date = models.DateField(default=datetime.date.today)
    one_day = models.BooleanField(default=True)
    end_date = models.DateField(default=datetime.date.today)
    duration = models.DurationField(null=True, blank=True)
    intensity = models.CharField(
        max_length = 2,
        choices = INTENSITY_CHOICES,
        default = 'L'
    )
    dist = MeasurementField(
        null=True,
        blank=True,
        default=0,
        measurement=Distance,
        unit_choices=(("mi", "mi"), ("km", "km"), ("ft", "ft"), ("m", "m"))
    )

    raw_count = models.PositiveIntegerField(default = 0)
    second_raw_count = models.PositiveIntegerField(default = 0)
    raw_set = models.PositiveIntegerField(default = 1)
    raw_rep = models.PositiveIntegerField(default = 1)
    weight = MeasurementField(
        null=True,
        blank=True,
        default=0,
        measurement=Weight,
        unit_choices=(("lb", "lb"), ("kg", "kg"))
    )

    def get_year(self):
        return self.start_date.strftime('%Y')
    def get_month(self):
        return self.start_date.strftime('%m')
    def get_day(self):
        return self.start_date.strftime('%d')

BASE_DIR = Path(__file__).resolve().parent.parent
ICON_CHOICES = sorted([(fn, fn) for fn in os.listdir(BASE_DIR / 'static' / 'icons')])

class Achievement(models.Model):
    title = models.CharField(max_length=30, default='')
    description = models.TextField(default='')
    icon = models.CharField(
        max_length=100, 
        choices = ICON_CHOICES
    )
    has_start_date = models.BooleanField(default=False)
    start_date = models.DateField(default=datetime.date.today)
    has_end_date = models.BooleanField(default=False)
    end_date = models.DateField(default=datetime.date.today)
    has_specific_workoutType = models.BooleanField(default=False)
    specific_workoutType = models.ForeignKey(WorkoutType, on_delete=models.CASCADE, null=True, blank=True)
    has_second_specific_workoutType = models.BooleanField(default=False)
    second_specific_workoutType = models.ForeignKey(WorkoutType, on_delete=models.CASCADE, blank=True, related_name='sswt', null=True)
    has_workout_count_min = models.BooleanField(default=False)
    workout_count_min = models.PositiveIntegerField(blank = True, null = True)
    has_specific_WorkoutTypeCount = models.BooleanField(default=False)
    specific_WorkoutTypeCount = models.ForeignKey(WorkoutTypeCount, on_delete=models.CASCADE, null=True, blank=True)
    specific_WorkoutTypeCount_min = models.PositiveIntegerField(blank = True, null = True)
    has_second_specific_WorkoutTypeCount = models.BooleanField(default=False)
    second_specific_WorkoutTypeCount = models.ForeignKey(WorkoutTypeCount, on_delete=models.CASCADE, blank=True, related_name='sswtc', null=True)
    second_specific_WorkoutTypeCount_min = models.PositiveIntegerField(blank = True, null=True)
    has_min_single_weight = models.BooleanField(default=False)
    min_single_weight = MeasurementField(
        null=True,
        blank=True,
        default=0,
        measurement=Weight,
        unit_choices=(("lb", "lb"), ("kg", "kg"))
    )
    has_min_total_weight = models.BooleanField(default=False)
    min_total_weight = MeasurementField(
        null=True,
        blank=True,
        default=0,
        measurement=Weight,
        unit_choices=(("lb", "lb"), ("kg", "kg"))
    )
    has_min_reps = models.BooleanField(default=False)
    min_reps = models.PositiveIntegerField(blank = True, null = True)
    has_min_single_distance = models.BooleanField(default=False)
    min_single_distance = MeasurementField(
        null=True,
        blank=True,
        default=0,
        measurement=Distance,
        unit_choices=(("mi", "mi"), ("km", "km"), ("ft", "ft"), ("m", "m"))
    )
    has_min_total_distance = models.BooleanField(default=False)
    min_total_distance = MeasurementField(
        null=True,
        blank=True,
        default=0,
        measurement=Distance,
        unit_choices=(("mi", "mi"), ("km", "km"), ("ft", "ft"), ("m", "m"))
    )
    has_min_single_duration = models.BooleanField(default=False)
    min_single_duration = models.DurationField(null=True, blank=True)
    has_min_total_duration = models.BooleanField(default=False)
    min_total_duration = models.DurationField(null=True, blank=True)
    points = models.PositiveIntegerField(default = 10, blank = True, null = True)
    has_max_pace = models.BooleanField(default=False)
    max_pace_per_mile = models.DurationField(null=True, blank=True)

class City(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'cities'