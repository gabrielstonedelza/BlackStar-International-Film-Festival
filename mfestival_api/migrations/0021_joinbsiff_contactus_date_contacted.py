# Generated by Django 4.0.4 on 2022-07-08 08:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mfestival_api', '0020_remove_contactus_mobile_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinBsiff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='contactus',
            name='date_contacted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]