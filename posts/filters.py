from codecs import lookup_error
from dataclasses import fields
from django.forms import ModelChoiceField
import django_filters as filters
from .models import Post
from .forms import INDUSTRY_CHOICES


class PostFilter(filters.FilterSet):
    # date range filter
    # start_date = DateFilter(field_name='created', lookup_expr='gre')
    # end_date = DateFilter(field_name='created', lookup_expr='lte')

    job_description = filters.CharFilter(
        field_name='job_description', lookup_expr='icontains')
    industry = filters.ChoiceFilter( choices= INDUSTRY_CHOICES,field_name='industry', lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['location',
        'industry',
        'specialization',]
        # fields = '__all__'
        exclude = ['company_name', 'website', 'company_pic']
