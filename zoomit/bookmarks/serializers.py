from rest_framework import serializers
from .models import User, UrlObject

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class UrlObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlObject
        fields = ['id', 'user', 'url', 'active']
