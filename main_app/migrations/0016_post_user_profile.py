# Generated by Django 4.2.3 on 2023-07-19 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_remove_userprofile_school_class_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user_profile',
            field=models.ManyToManyField(to='main_app.userprofile'),
        ),
    ]