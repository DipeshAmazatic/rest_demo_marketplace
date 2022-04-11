from rest_framework import serializers
from product.models import Company

class CompanySerializer(serializers.ModelSerializer):
    """
    Company serializer
    """
    class Meta:
        model = Company
        fields = ('__all__')