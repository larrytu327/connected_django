# Generated by Django 4.2.3 on 2023-07-18 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_messageboard_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messageboard',
            name='posts',
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField(max_length=750)),
                ('messageboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='main_app.messageboard')),
            ],
        ),
    ]
