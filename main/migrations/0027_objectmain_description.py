# Generated by Django 5.1 on 2024-08-25 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_alter_objectmain_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='objectmain',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
