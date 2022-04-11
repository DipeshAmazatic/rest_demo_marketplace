import email
from rest_framework import viewsets, permissions
from ..serializers import (VariantSerializer)
from product.models import ProductVariants
from ..permissions import ProductPermission

class VariantViewSet(viewsets.ModelViewSet):
    """
    CURD operation on Product Variant viewsets
    """
    queryset = ProductVariants.objects.all()
    permission_classes=(permissions.IsAuthenticated, ProductPermission)
    serializer_class=VariantSerializer
        
    