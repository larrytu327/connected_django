# Generated by Django 4.2.3 on 2023-07-19 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_userprofile_messageboard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='messageboard',
        ),
        migrations.AddField(
            model_name='messageboard',
            name='user_profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.userprofile'),
        ),
    ]
