# Generated by Django 4.0.4 on 2022-07-09 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mfestival_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submitfilm',
            name='category',
            field=models.CharField(choices=[('Documentary Film', 'Documentary Film'), ('Feature Film', 'Feature Film'), ('Short Film', 'Short Film'), ('Student Film', 'Student Film'), ('Women in Film', 'Women in Film'), ('Animated Film', 'Animated Film'), ('African Films', 'African Films')], default='Short Film', max_length=70),
        ),
    ]
