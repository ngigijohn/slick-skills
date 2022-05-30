from codecs import lookup_error
import django_filters
from django_filters import DateFilter, CharFilter
from .models import Post


class PostFilter(django_filters.FilterSet):
    # date range filter
    # start_date = DateFilter(field_name='created', lookup_expr='gre')
    # end_date = DateFilter(field_name='created', lookup_expr='lte')

    job_description = CharFilter(
        field_name='job_description', lookup_expr='icontains')

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['company_name', 'website']
