from rest_framework import viewsets, permissions
from ..serializers import (SpecificationSerializer)
from product.models import ProductSpecification
from ..permissions import ProductPermission

class SpecificationViewSet(viewsets.ModelViewSet):
    """
    CURD operation on Specification viewsets
    """
    queryset = ProductSpecification.objects.all()
    permission_classes=(permissions.IsAuthenticated, ProductPermission)
    serializer_class=SpecificationSerializer

    