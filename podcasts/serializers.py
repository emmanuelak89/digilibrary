from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import *

class PodcastSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.CharField()
    class Meta:
        model = PodcastPack
        fields = '__all__'

class PodcastLikeSerializer(serializers.ModelSerializer):
    podcast = serializers.CharField()
    user = serializers.CharField()
    class Meta:
        model = UserPodcastLike
        fields = '__all__'

class PodcastListSerializer(serializers.ModelSerializer):
    podcast = serializers.CharField()
    user = serializers.CharField()
    class Meta:
        model = UserPodcastList
        fields = '__all__'