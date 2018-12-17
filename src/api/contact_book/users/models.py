from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    UserManager as DjangoUserManager
)
from django.db import models

from contact_book.models import TimestampedModel


class UserManager(DjangoUserManager):
    """"
    User manager
    """
    def _create(self, email, password, **kwargs):
        email = super().normalize_email(email)
        user = User(email=email, username=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        email = super().normalize_email(email)
        user = self._create(email=email, password=password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(TimestampedModel, AbstractBaseUser, PermissionsMixin):
    """
        Represents a user within the Contact Book App.
    """

    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, null=True, blank=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['email']

    def get_short_name(self):
        return self.email
