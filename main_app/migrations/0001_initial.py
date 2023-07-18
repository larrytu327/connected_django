# Generated by Django 4.2.3 on 2023-07-18 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessageBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=300)),
                ('date_added', models.TimeField(auto_now_add=True)),
                ('posts', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['date_added', 'subject'],
            },
        ),
    ]
