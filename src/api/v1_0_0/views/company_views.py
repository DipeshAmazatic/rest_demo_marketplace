from rest_framework import viewsets, permissions
from ..serializers import (CompanySerializer,)
from product.models import Company
from ..permissions import CompanyPermission
class CompanyViewSet(viewsets.ModelViewSet):
    """
    CURD operation on Company viewsets
    """
    queryset = Company.objects.all()
    permission_classes=(permissions.IsAuthenticated, CompanyPermission)
    serializer_class=CompanySerializer

    