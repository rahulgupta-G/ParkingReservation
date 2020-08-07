# Generated by Django 2.1.7 on 2019-04-01 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('driver_name', models.CharField(max_length=30)),
                ('driver_license', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('vehicle_number', models.CharField(max_length=10)),
                ('checkin_time', models.DateTimeField()),
            ],
        ),
    ]
