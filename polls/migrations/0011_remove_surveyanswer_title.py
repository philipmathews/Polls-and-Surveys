# Generated by Django 2.0.4 on 2018-04-23 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20180423_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyanswer',
            name='title',
        ),
    ]
