# Generated by Django 3.2 on 2021-05-19 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper_project', '0002_auto_20210519_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='bangladesh',
            name='publish_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='entertainment',
            name='publish_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='international',
            name='publish_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='sports',
            name='publish_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='trade',
            name='publish_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
