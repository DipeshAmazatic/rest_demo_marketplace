from django.contrib.auth.models import UserManager
from django.contrib.auth.hashers import make_password

class UsersManager(UserManager):

    """Custom manager for EmailOrMobileUser."""

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save an EmailUser with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save an EmailUser with the given email and password.
        """
        return super().create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save an EmailUser with the given email and password.
        """
        return super().create_superuser(email, password, **extra_fields)
