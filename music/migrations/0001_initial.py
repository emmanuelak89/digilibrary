# Generated by Django 4.0.4 on 2022-05-10 07:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicPack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('genre', models.CharField(default='rock', max_length=20)),
                ('type', models.CharField(default='single', max_length=25)),
                ('description', models.CharField(default='no description', max_length=100, null=True)),
                ('uploaded_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PodcastPack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('genre', models.CharField(default='comedy', max_length=20)),
                ('description', models.CharField(default='no description', max_length=100, null=True)),
                ('uploaded_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VideoPack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('genre', models.CharField(default='thriller', max_length=20)),
                ('type', models.CharField(default='movie', max_length=25)),
                ('description', models.CharField(default='no description', max_length=100, null=True)),
                ('uploaded_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VideoRepo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_name', models.CharField(max_length=100)),
                ('document_src', models.FileField(blank=True, upload_to='file/')),
                ('videopack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.videopack')),
            ],
        ),
        migrations.CreateModel(
            name='UserVideoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.videopack')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserPodcastList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('podcast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.podcastpack')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserMusicList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artist', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listener', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PodcastRepo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_name', models.CharField(max_length=100)),
                ('document_src', models.FileField(blank=True, upload_to='file/')),
                ('podcastpack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.podcastpack')),
            ],
        ),
        migrations.CreateModel(
            name='MusicRepo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_name', models.CharField(max_length=100)),
                ('document_src', models.FileField(blank=True, upload_to='file/')),
                ('musicpack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.musicpack')),
            ],
        ),
    ]
