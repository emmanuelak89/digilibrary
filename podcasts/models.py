from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class PodcastPack(models.Model):
    name = models.CharField(max_length=50)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    genre = models.CharField(max_length=20, null=False, default='comedy')
    description = models.CharField(max_length=100,null=True,default='no description')
    uploaded_date = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(upload_to='images/', default='images/home-profile.jpg', null=True)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class PodcastRepo(models.Model):
    document_name = models.CharField(max_length=100)
    document_src = models.FileField(upload_to='file/', blank=True, null=False)
    podcastpack = models.ForeignKey(PodcastPack, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.document_name

class UserPodcastList(models.Model):
    podcast = models.ForeignKey(PodcastPack, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

class UserPodcastLike(models.Model):
    podcast = models.ForeignKey(PodcastPack, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
