from django.db import models
from django.urls.base import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    company_name = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    products_and_services = models.CharField(max_length=50, null=True, blank=True)
    contact = models.CharField(max_length=50, null=True, blank=True)
    application_requirements = models.CharField(max_length=50, null=True, blank=True)
    application_process = models.CharField(max_length=50, null=True, blank=True)
    application_deadline = models.CharField(max_length=50, null=True, blank=True)
    contact = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title
