# Generated by Django 3.1.4 on 2020-12-11 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_workout_sixth_exercise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='fifth_exercise',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='workout',
            name='first_exercise',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='workout',
            name='fourth_exercise',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='workout',
            name='notes',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='workout',
            name='second_exercise',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='workout',
            name='third_exercise',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
