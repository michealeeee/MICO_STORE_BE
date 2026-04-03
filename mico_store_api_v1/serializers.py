from .models import User
from rest_framework_mongoengine import serializers


class UserSerializer(serializers.DocumentSerializer):
    class Meta:
        model = User
        fields = '__all__'

from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()