# Generated by Django 5.1.4 on 2025-01-06 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourpackage',
            name='image',
            field=models.ImageField(default=0, upload_to='gallary'),
        ),
    ]
