# Generated by Django 5.0.7 on 2024-07-25 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_managers_surname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
