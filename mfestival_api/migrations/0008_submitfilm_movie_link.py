# Generated by Django 4.0.4 on 2022-07-03 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mfestival_api', '0007_alter_submitfilm_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='submitfilm',
            name='movie_link',
            field=models.TextField(blank=True),
        ),
    ]
