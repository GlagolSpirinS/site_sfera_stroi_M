# Generated by Django 5.1 on 2024-08-20 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_object_additional_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='object',
            name='additional_images',
        ),
    ]
