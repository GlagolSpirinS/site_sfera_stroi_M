# Generated by Django 5.1 on 2024-08-22 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_remove_object_additional_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='object',
            name='image1',
            field=models.ImageField(default='path/image.jpg', upload_to='objectImg/'),
        ),
        migrations.AddField(
            model_name='object',
            name='image2',
            field=models.ImageField(default='path/image.jpg', upload_to='objectImg/'),
        ),
        migrations.AddField(
            model_name='object',
            name='image3',
            field=models.ImageField(default='path/image.jpg', upload_to='objectImg/'),
        ),
        migrations.AddField(
            model_name='object',
            name='image4',
            field=models.ImageField(default='path/image.jpg', upload_to='objectImg/'),
        ),
        migrations.AddField(
            model_name='object',
            name='image5',
            field=models.ImageField(default='path/image.jpg', upload_to='objectImg/'),
        ),
        migrations.AddField(
            model_name='object',
            name='image6',
            field=models.ImageField(default='path/image.jpg', upload_to='objectImg/'),
        ),
        migrations.AddField(
            model_name='object',
            name='image7',
            field=models.ImageField(default='path/image.jpg', upload_to='objectImg/'),
        ),
    ]
