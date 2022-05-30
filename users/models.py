
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid
from .managers import CustomAccountManager

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(_("Email address"), unique=True, max_length=254)
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    institution = models.CharField(_("Institution"), max_length=150)
    major = models.CharField(_("Major"), max_length=150)
    profile_pic = models.ImageField(blank=True, null=True, default='default.png', upload_to='profile_pics')
    phone_number = models.CharField(_("Phone number"), max_length=50)
    def __str__(self):
        return self.user.username + "Profile"
