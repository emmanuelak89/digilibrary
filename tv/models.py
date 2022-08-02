from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class VideoPack(models.Model):
    name = models.CharField(max_length=50)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    genre = models.CharField(max_length=20, null=False, default='thriller')
    type = models.CharField(max_length=25, null=False, default='movie')
    description = models.CharField(max_length=100,null=True,default='no description')
    uploaded_date = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(upload_to='images/', default='images/home-profile.jpg', null=True)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class VideoRepo(models.Model):
    document_name = models.CharField(max_length=100)
    document_src = models.FileField(upload_to='file/', blank=True, null=False)
    videopack = models.ForeignKey(VideoPack, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.document_name

class UserVideoLike(models.Model):
    show = models.ForeignKey(VideoPack, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

class UserVideoList(models.Model):
    show = models.ForeignKey(VideoPack, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
