"""
Product related model
"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User
# Create your models here.

class Company(models.Model):
    """
    company model
    """
    name = models.CharField(_('company name'), max_length=50, null=False, blank=False)

    def __str__(self):
        return "{}".format(self.name)

class Product(models.Model):
    """
    product model
    """
    name = models.CharField(_('product name'), max_length=100, null=False, blank=False)
    company = models.OneToOneField(Company, related_name="company", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.company, self.name)

class ProductVariants(models.Model):
    """
    product variants model
    """
    rating_choice = [
                ('1', 1),
                ('2', 2),
                ('3', 3),
                ('4', 4),
                ('5', 5),
    ]
    product = models.ForeignKey(Product, related_name="product", on_delete=models.CASCADE)
    name = models.CharField(_('variants name'), max_length=100, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)
    variant_type = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(max_digits=100, decimal_places=4)
    feature = models.CharField(max_length=200, null=False, blank=False)
    rating = models.CharField(max_length=5, choices=rating_choice)

    def __str__(self):
        return "{} {}".format(self.product, self.variant_type)

class ProductSpecification(models.Model):
    """
    product specification model
    """
    variant = models.OneToOneField(ProductVariants, related_name="variant", on_delete=models.CASCADE)#related_name='productspecifications'
    specification_details = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return "{}".format(self.specification_details)
