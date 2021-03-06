# Generated by Django 3.1.4 on 2020-12-12 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20201211_1253'),
        ('app', '0008_auto_20201212_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progresspicture',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.userprofile'),
        ),
        migrations.AlterField(
            model_name='workout',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.userprofile'),
        ),
    ]
