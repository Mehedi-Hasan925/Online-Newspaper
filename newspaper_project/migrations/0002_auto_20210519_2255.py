# Generated by Django 3.2 on 2021-05-19 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper_project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bangladesh',
            name='publish_time',
        ),
        migrations.RemoveField(
            model_name='entertainment',
            name='publish_time',
        ),
        migrations.RemoveField(
            model_name='international',
            name='publish_time',
        ),
        migrations.RemoveField(
            model_name='sports',
            name='publish_time',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='publish_time',
        ),
    ]
