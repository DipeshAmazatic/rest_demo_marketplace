
"""
User models
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (AbstractUser,)
from users.manager import UsersManager
# Create your models here.

class User(AbstractUser):
    """
    User model
    """

    username = None
    name = models.CharField(_('full name'),max_length=30)
    email = models.EmailField(_('email address'), unique=True)
    phone_no = models.CharField(_('phone number'),max_length=10,unique=True)
    is_email_verified = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_no']
    objects = UsersManager()

    def __str__(self):
        return "{}".format(self.email)
