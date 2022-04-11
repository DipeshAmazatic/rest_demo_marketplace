from rest_framework import serializers
from product.models import ProductSpecification
class SpecificationSerializer(serializers.ModelSerializer):
    """
    specification serializer
    """
    class Meta:
        model = ProductSpecification
        fields = ('specification_details',)