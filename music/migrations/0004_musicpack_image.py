# Generated by Django 4.0.4 on 2022-05-12 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_remove_podcastrepo_podcastpack_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicpack',
            name='image',
            field=models.ImageField(default='images/home-profile.jpg', null=True, upload_to='images/'),
        ),
    ]
