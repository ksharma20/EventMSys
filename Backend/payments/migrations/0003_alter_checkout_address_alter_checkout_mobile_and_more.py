# Generated by Django 4.0.1 on 2022-02-08 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_checkout_pytmcheck'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='address',
            field=models.TextField(default='Not Added'),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='mobile',
            field=models.IntegerField(default='0000'),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='name',
            field=models.CharField(default='guest', max_length=50),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='pin_code',
            field=models.IntegerField(default='0000'),
        ),
    ]