# Generated by Django 2.0.4 on 2018-06-24 13:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 24, 15, 30, 14, 877068)),
        ),
    ]
