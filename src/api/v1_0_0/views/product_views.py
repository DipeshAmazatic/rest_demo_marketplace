from rest_framework import viewsets, permissions
from ..serializers import (ProductSerializer,)
from product.models import Product
from ..permissions import ProductPermission

class ProductViewSet(viewsets.ModelViewSet):
    """
    CURD operation on Product viewsets
    """
    queryset = Product.objects.all()
    permission_classes=(permissions.IsAuthenticated, ProductPermission)
    serializer_class=ProductSerializer
    
    