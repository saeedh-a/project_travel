# Generated by Django 5.1.4 on 2025-01-06 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_tourpackage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourpackage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='gallary'),
        ),
    ]
