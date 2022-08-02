from rest_framework import serializers
from .models import *

class VideoSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.CharField()
    class Meta:
        model = VideoPack
        fields = '__all__'

class VideoLikeSerializer(serializers.ModelSerializer):
    music = serializers.CharField()
    user = serializers.CharField()
    class Meta:
        model = UserVideoLike
        fields = '__all__'

class VideoListSerializer(serializers.ModelSerializer):
    music = serializers.CharField()
    user = serializers.CharField()
    class Meta:
        model = UserVideoList
        fields = '__all__'