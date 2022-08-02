# Generated by Django 4.0.4 on 2022-05-12 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_alter_usermusiclist_artist_alter_usermusiclist_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='podcastrepo',
            name='podcastpack',
        ),
        migrations.RemoveField(
            model_name='userpodcastlike',
            name='podcast',
        ),
        migrations.RemoveField(
            model_name='userpodcastlike',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userpodcastlist',
            name='podcast',
        ),
        migrations.RemoveField(
            model_name='userpodcastlist',
            name='user',
        ),
        migrations.RemoveField(
            model_name='uservideolike',
            name='show',
        ),
        migrations.RemoveField(
            model_name='uservideolike',
            name='user',
        ),
        migrations.RemoveField(
            model_name='uservideolist',
            name='show',
        ),
        migrations.RemoveField(
            model_name='uservideolist',
            name='user',
        ),
        migrations.RemoveField(
            model_name='videopack',
            name='uploaded_by',
        ),
        migrations.RemoveField(
            model_name='videorepo',
            name='videopack',
        ),
        migrations.DeleteModel(
            name='PodcastPack',
        ),
        migrations.DeleteModel(
            name='PodcastRepo',
        ),
        migrations.DeleteModel(
            name='UserPodcastLike',
        ),
        migrations.DeleteModel(
            name='UserPodcastList',
        ),
        migrations.DeleteModel(
            name='UserVideoLike',
        ),
        migrations.DeleteModel(
            name='UserVideoList',
        ),
        migrations.DeleteModel(
            name='VideoPack',
        ),
        migrations.DeleteModel(
            name='VideoRepo',
        ),
    ]
