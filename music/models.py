from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class MusicPack(models.Model):
    name = models.CharField(max_length=50)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    genre = models.CharField(max_length=20, null=False, default='rock')
    type = models.CharField(max_length=25, null=False, default='single')
    description = models.CharField(max_length=100,null=True,default='no description')
    uploaded_date = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(upload_to='images/', default='images/home-profile.jpg', null=True)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class MusicRepo(models.Model):
    document_name = models.CharField(max_length=100)
    document_src = models.FileField(upload_to='file/', blank=True, null=False)
    musicpack = models.ForeignKey(MusicPack, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.document_name


class UserMusicList(models.Model):
    music = models.ForeignKey(MusicPack, on_delete=models.CASCADE, null=False, related_name='streamed', default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='streamer')


class UserMusicLike(models.Model):
    music = models.ForeignKey(MusicPack, on_delete=models.CASCADE, null=False, related_name='artist', default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='listener')
