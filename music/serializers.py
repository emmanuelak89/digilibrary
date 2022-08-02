from rest_framework import serializers
from .models import *

class MusicSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.CharField()
    class Meta:
        model = MusicPack
        fields = '__all__'

class MusicLikeSerializer(serializers.ModelSerializer):
    music = serializers.CharField()
    user = serializers.CharField()
    class Meta:
        model = UserMusicLike
        fields = '__all__'

class MusicListSerializer(serializers.ModelSerializer):
    music = serializers.CharField()
    user = serializers.CharField()
    class Meta:
        model = UserMusicList
        fields = '__all__'