# Generated by Django 4.2.3 on 2023-07-19 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_remove_messageboard_date_added_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='school_class',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='school_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='main_app.schoolclass'),
        ),
    ]
