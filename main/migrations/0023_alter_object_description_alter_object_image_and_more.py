# Generated by Django 5.1 on 2024-08-23 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_remove_object_image10_remove_object_image11_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='object',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='objectImg/'),
        ),
        migrations.AlterField(
            model_name='object',
            name='image1',
            field=models.ImageField(blank=True, default='path/image.jpeg', null=True, upload_to='objectImg/'),
        ),
        migrations.AlterField(
            model_name='object',
            name='image2',
            field=models.ImageField(blank=True, default='path/image.jpeg', null=True, upload_to='objectImg/'),
        ),
        migrations.AlterField(
            model_name='object',
            name='image3',
            field=models.ImageField(blank=True, default='path/image.jpeg', null=True, upload_to='objectImg/'),
        ),
        migrations.AlterField(
            model_name='object',
            name='image4',
            field=models.ImageField(blank=True, default='path/image.jpeg', null=True, upload_to='objectImg/'),
        ),
        migrations.AlterField(
            model_name='object',
            name='image5',
            field=models.ImageField(blank=True, default='path/image.jpeg', null=True, upload_to='objectImg/'),
        ),
        migrations.AlterField(
            model_name='object',
            name='image6',
            field=models.ImageField(blank=True, default='path/image.jpeg', null=True, upload_to='objectImg/'),
        ),
        migrations.AlterField(
            model_name='object',
            name='image7',
            field=models.ImageField(blank=True, default='path/image.jpeg', null=True, upload_to='objectImg/'),
        ),
        migrations.AlterField(
            model_name='object',
            name='image8',
            field=models.ImageField(blank=True, default='path/image.jpeg', null=True, upload_to='objectImg/'),
        ),
        migrations.AlterField(
            model_name='object',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
