# Generated by Django 2.0.4 on 2018-06-23 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addedseriesmodel',
            options={'ordering': ('-date_started',), 'verbose_name': 'Added Series', 'verbose_name_plural': 'Added Series'},
        ),
        migrations.AlterModelOptions(
            name='episodemodel',
            options={'ordering': ('-date_added',), 'verbose_name': 'Episode', 'verbose_name_plural': 'Episodes'},
        ),
        migrations.AlterModelOptions(
            name='seasonmodel',
            options={'ordering': ('-date_added',), 'verbose_name': 'Season', 'verbose_name_plural': 'Seasons'},
        ),
        migrations.AlterModelOptions(
            name='seriesmodel',
            options={'ordering': ('-date_added',), 'verbose_name': 'Series', 'verbose_name_plural': 'Series'},
        ),
    ]
