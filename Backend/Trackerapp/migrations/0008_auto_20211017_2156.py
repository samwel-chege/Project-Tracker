# Generated by Django 3.2.8 on 2021-10-17 18:56

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Trackerapp', '0007_remove_student_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_image',
            field=cloudinary.models.CloudinaryField(blank=True, default=0, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='student',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(blank=True, default=0, max_length=255, null=True, verbose_name='image'),
        ),
    ]