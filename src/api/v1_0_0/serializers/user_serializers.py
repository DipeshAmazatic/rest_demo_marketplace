from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    """
    User serializer
    """
    class Meta:
        model = User
        fields = ('name','email','phone_no','is_email_verified')