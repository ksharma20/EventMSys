# Generated by Django 4.0.1 on 2022-02-04 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('pin_code', models.IntegerField()),
                ('paid', models.BooleanField(default=False)),
                ('amount', models.IntegerField(default=0)),
                ('order_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
