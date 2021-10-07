# Generated by Django 3.2.8 on 2021-10-06 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trackerapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='cohort',
            name='details',
            field=models.CharField(blank=True, default='A Moringa cohort.', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='cohort',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='cohort',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project', to='Trackerapp.cohort'),
        ),
        migrations.AddField(
            model_name='project',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project', to='Trackerapp.language'),
        ),
    ]