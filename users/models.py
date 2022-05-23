
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import CustomAccountManager

# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin, ):
    email = models.EmailField(_("Email address"), unique=True, max_length=254)
    username = models.CharField(unique=True, max_length=150)
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    institution = models.CharField(_("Institution"), max_length=150)
    major = models.CharField(_("Major"), max_length=150)
    phone_number = models.CharField(_("Phone number"), max_length=50)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # REQUIRED_FIELDS = ['username', 'email']

    objects = CustomAccountManager()

    def __str__(self):
        return self.username
