# Generated by Django 5.0.7 on 2024-07-28 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_object'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='image',
            field=models.ImageField(upload_to='objectImg/'),
        ),
    ]
