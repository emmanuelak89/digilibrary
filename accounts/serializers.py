from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import *

class BioSerializer(serializers.ModelSerializer):
    user = serializers.CharField()
    class Meta:
        model = Bio
        fields = '__all__'

