# Generated by Django 4.0.4 on 2022-07-03 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mfestival_api', '0005_alter_submitfilm_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='submitfilm',
            name='genre',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
