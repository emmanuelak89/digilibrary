# Generated by Django 4.0.4 on 2022-05-16 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0002_podcastpack_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcastpack',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]