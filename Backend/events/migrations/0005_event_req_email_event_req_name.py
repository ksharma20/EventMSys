# Generated by Django 4.0.1 on 2022-02-08 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_rename_address_event_req_mobile_remove_event_mobile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='req_email',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='req_name',
            field=models.BooleanField(default=False),
        ),
    ]
