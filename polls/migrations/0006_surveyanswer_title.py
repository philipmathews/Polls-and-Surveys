# Generated by Django 2.0.4 on 2018-04-23 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_remove_surveyanswer_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyanswer',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Surveytitle'),
            preserve_default=False,
        ),
    ]
