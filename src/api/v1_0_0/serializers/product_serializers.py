from rest_framework import serializers
from .user_serializers import UserSerializer
from product.models import Product
from .company_serializers import CompanySerializer

class ProductSerializer(serializers.ModelSerializer):
    """
    Product serializer
    """
    company_info = CompanySerializer(required=False, source ='company')
    user_info = UserSerializer(required=False, source ='user')
    def create(self, validated_data):
        print(self.context['request'].user)
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
    class Meta:
        model = Product
        #fields = ('id', 'name', 'company_info', 'user_info')
        exclude = ('user',)