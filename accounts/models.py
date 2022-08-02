from django.db import models
from django.contrib.auth.models import User

class Bio(models.Model):
    email = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=35)
    shortbio = models.CharField(max_length=90, default='null', null=True)
    image = models.ImageField(upload_to='images/', default='images/home-profile.jpg', null=True)
    phone = models.IntegerField(null=True)
    role = models.CharField(max_length=15,default='user')
    total_likes = models.IntegerField(null=True,default=0)
    total_saved = models.IntegerField(null=True, default=0)
    total_viewed = models.IntegerField(null=True, default=0)
    def __str__(self):
        return self.name


