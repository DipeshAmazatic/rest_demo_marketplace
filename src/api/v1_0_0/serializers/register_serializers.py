from rest_framework import serializers
from users.models import User
from django.contrib.auth import password_validation
from django.contrib.auth.models import BaseUserManager

class RegisterSerializer(serializers.ModelSerializer):
    """
    Register serializer 
    """
    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password', 'phone_no')

    def validate_email(self, value):
        """
        validate email
        """
        user = User.objects.filter(email=value)
        if user:
            raise serializers.ValidationError("Email is already taken")
        return BaseUserManager.normalize_email(value)

    def validate_password(self, value):
        """
        validate password
        """
        password_validation.validate_password(value)
        return value
