# Generated by Django 5.1.4 on 2025-01-08 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_alter_booking_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='total_price',
            field=models.DecimalField(decimal_places=True, max_digits=10, null=True),
        ),
    ]
