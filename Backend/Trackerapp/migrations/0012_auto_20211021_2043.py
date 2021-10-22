# Generated by Django 3.2.8 on 2021-10-21 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trackerapp', '0011_merge_0008_auto_20211017_2325_0010_auto_20211019_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_verified',
        ),
        migrations.RemoveField(
            model_name='project',
            name='scrum',
        ),
        migrations.AddField(
            model_name='student',
            name='github_profile',
            field=models.URLField(blank=True, null=True),
        ),
    ]