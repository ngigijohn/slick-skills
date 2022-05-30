from django.db import models

from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    company_pic = models.ImageField(
        default='company_pic.png', blank=True, upload_to='company_pics')
    company_name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    industry = models.CharField(max_length=100, null=True, blank=True)
    products_and_services = models.CharField(
        max_length=50, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=300, null=True, blank=True)
    job_title = models.CharField(max_length=300, null=True, blank=True)
    job_type = models.CharField(max_length=100, null=True, blank=True)
    specialization = models.CharField(max_length=150, null=True, blank=True)
    job_description = models.CharField(max_length=500, null=True, blank=True)
    education_and_experience = models.CharField(
        max_length=500, null=True, blank=True)
    application_requirements = models.CharField(
        max_length=500, null=True, blank=True)
    application_process = models.CharField(
        max_length=600, null=True, blank=True)
    application_deadline = models.CharField(
        max_length=100, null=True, blank=True)
    bookmarks = models.ManyToManyField(
        User, related_name='bookmark')

    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.company_name + ", " + self.industry
