# Generated by Django 3.2.8 on 2021-10-19 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Trackerapp', '0010_auto_20211019_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_verified',
        ),
    ]
