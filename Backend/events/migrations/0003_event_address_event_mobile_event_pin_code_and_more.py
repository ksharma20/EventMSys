# Generated by Django 4.0.1 on 2022-02-08 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_remove_event_end_date_remove_event_end_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='mobile',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='pin_code',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='req_addr',
            field=models.BooleanField(default=False),
        ),
    ]