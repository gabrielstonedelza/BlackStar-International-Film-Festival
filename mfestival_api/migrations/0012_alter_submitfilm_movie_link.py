# Generated by Django 4.0.4 on 2022-07-03 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mfestival_api', '0011_remove_submitfilm_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submitfilm',
            name='movie_link',
            field=models.URLField(blank=True),
        ),
    ]
