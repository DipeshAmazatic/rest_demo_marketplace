"""
product related admin
"""

from django.contrib import admin
from .models import (Company, Product, ProductSpecification, ProductVariants)
# Register your models here.

admin.site.register(Company)
admin.site.register(Product)
admin.site.register(ProductVariants)
admin.site.register(ProductSpecification)
