# Generated by Django 5.1 on 2024-08-16 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_jobs_opisaniye'),
    ]

    operations = [
        migrations.AddField(
            model_name='object',
            name='is_ready',
            field=models.BooleanField(default=False),
        ),
    ]
