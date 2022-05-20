from django.db import models
from django.urls.base import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    title = models.CharField(max_length=250)
    company_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    products_and_services = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    application_requirements = models.CharField(max_length=50)
    application_process = models.CharField(max_length=50)
    application_deadline = models.CharField(max_length=50)
    contact = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
