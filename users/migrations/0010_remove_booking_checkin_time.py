# Generated by Django 2.1.7 on 2019-04-01 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='checkin_time',
        ),
    ]
