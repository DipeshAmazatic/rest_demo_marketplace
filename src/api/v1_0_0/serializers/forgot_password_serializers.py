from rest_framework import serializers

class ForgotPasswordSerializer(serializers.Serializer):
    """
    Forgot password serializer
    """
    email = serializers.EmailField(required=True)