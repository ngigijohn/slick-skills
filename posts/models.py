from django.db import models
from django.urls.base import reverse
from users.models import CustomUser


class Post(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    industry = models.CharField(max_length=100, null=True, blank=True)
    specialization = models.CharField(max_length=150, null=True, blank=True)
    products_and_services = models.CharField(
        max_length=50, null=True, blank=True)
    contact = models.CharField(max_length=300, null=True, blank=True)
    application_requirements = models.CharField(
        max_length=500, null=True, blank=True)
    application_process = models.CharField(
        max_length=600, null=True, blank=True)
    application_deadline = models.CharField(
        max_length=100, null=True, blank=True)
    bookmarks = models.ManyToManyField(
        CustomUser, related_name='bookmark', blank=True)

    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.company_name + ", " + self.industry
