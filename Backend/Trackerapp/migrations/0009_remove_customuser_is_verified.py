# Generated by Django 3.2.8 on 2021-10-20 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Trackerapp', '0008_auto_20211017_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_verified',
        ),
    ]
