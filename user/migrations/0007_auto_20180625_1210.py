# Generated by Django 2.0.4 on 2018-06-25 10:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20180625_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 25, 12, 10, 24, 784510)),
        ),
    ]