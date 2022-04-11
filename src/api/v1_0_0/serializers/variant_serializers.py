from rest_framework import serializers
from product.models import ProductVariants
from .product_serializers import ProductSerializer
from .specification_serializers import SpecificationSerializer

class VariantSerializer(serializers.ModelSerializer):
    """
    Product variant serializer
    """
    product_info = ProductSerializer(required=False, source ='product')
    variant_info = SpecificationSerializer(required=False, source ='variant')
    class Meta:
        model = ProductVariants
        fields = ('id', 'name', 'description', 'variant_type', 
                    'price', 'feature', 'rating', 'product_info', 'variant_info')
        