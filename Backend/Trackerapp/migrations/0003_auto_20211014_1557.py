# Generated by Django 3.2.8 on 2021-10-14 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trackerapp', '0002_auto_20211014_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='second_name',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]
