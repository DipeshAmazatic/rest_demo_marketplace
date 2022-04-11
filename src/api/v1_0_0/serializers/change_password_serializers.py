from rest_framework import serializers
from django.contrib.auth import password_validation

class ChangePasswordSerializer(serializers.Serializer):
    """
    Change password serializer
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_current_password(self, value):
        """
        Validate current password
        """
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('Current password does not match')
        return value

    def validate_new_password(self, value):
        """
        Validate new password
        """
        password_validation.validate_password(value)
        return value
