# Generated by Django 3.1.7 on 2021-04-08 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_app', '0034_auto_20210405_0408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=30)),
                ('description', models.TextField(default='')),
                ('icon', models.CharField(choices=[('fitness-biceps.png', 'fitness-biceps.png'), ('fitness-bicycle-1.png', 'fitness-bicycle-1.png'), ('fitness-bicycle-2.png', 'fitness-bicycle-2.png')], max_length=100)),
            ],
        ),
    ]
