# Generated by Django 4.2.3 on 2023-07-18 23:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_messageboard_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schoolclass',
            name='user_profile',
        ),
        migrations.AddField(
            model_name='messageboard',
            name='date_added',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='school_class',
            field=models.ManyToManyField(to='main_app.schoolclass'),
        ),
    ]
