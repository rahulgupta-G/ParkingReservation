# Generated by Django 2.1.7 on 2019-04-04 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_booking_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='vehicle_size',
            field=models.CharField(choices=[('Personal vehicle', 'Personal vehicle'), ('Commercial vehicle', 'Commercial vehicle'), ('Sport utility vehicle', 'Sport utility vehicle'), ('Special purpose vehicle', 'Special purpose vehicle')], default='Personal vehicle', max_length=1),
        ),
    ]
